from flask import Flask, request, jsonify, session, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
import os
import secrets
from bson import json_util, ObjectId
import json
import random
import string
from flask_mail import Mail
from flask_mail import Message
from detoxify import Detoxify
import re

app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "http://localhost:5174"}}, supports_credentials=True)

app.secret_key = secrets.token_hex(24)
app.config['MONGO_URI'] = 'mongodb+srv://23_DpMParums:J3imyzZW2lCp3mNx@uwork.wlvyybo.mongodb.net/?retryWrites=true&w=majority&appName=Uwork'
mongo = PyMongo(app)
CORS(app, supports_credentials=True)

client = MongoClient(app.config['MONGO_URI'])
db = client.Uwork
jobAdvert = db.JobAdvert
users = db.Register
applications = db.applications
tokenlist = db.tokenlist
collection = db['applications'] 

#Mailing configuration

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'work4uauto@gmail.com'  
app.config['MAIL_PASSWORD'] = 'acbi clew dqrz ywwj'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
otp_store = {}

mail = Mail(app)
mail.init_app(app)

# Directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Detoxify model - can be changed to multilingual or original
detoxify_model = Detoxify('multilingual')

def check_toxicity(message):
    """Check if a message is toxic using Detoxify."""
    scores = detoxify_model.predict(message)
    # Define threshold levels; adjust as necessary
    thresholds = {
        'toxicity': 0.65,
        'severe_toxicity': 0.35,
        'obscene': 0.8,
        'insult': 0.7,
        'threat': 0.7,
    }
    # Flag message as toxic if any score exceeds thresholds
    for category, threshold in thresholds.items():
        if scores.get(category, 0) >= threshold:
            return True
    return False

def is_nonsensical(message):
    """Check if the message contains nonsensical content."""
    
    # Check for repeated characters (e.g., 'fffff' or 'aaaaaaa')
    if re.search(r'(.)\1{4,}', message):  # Matches any character that repeats 5 or more times
        return True

    # Check for too few words
    words = message.split()
    if len(words) < 3:  # Require at least 3 words
        return True

    # Optional: Use a dictionary or a set of common words to check for validity
    common_words = set(["the", "is", "in", "and", "to", "a"])  # Expand this set as needed
    if not any(word in common_words for word in words):
        return True
    
    return False

@app.route('/apply', methods=['POST'])
def apply():
    # Get form data
    name = request.form.get('name')
    surname = request.form.get('surname')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')
    job_id = request.form.get('jobId')  # Retrieve the jobId

    # Check message toxicity
    if check_toxicity(message):
        return jsonify({"error": "Message contains toxic or offensive content."}), 400

    # Check if the message is nonsensical
    if is_nonsensical(message):
        return jsonify({"error": "Message contains nonsensical content."}), 400

    # Initialize a list to hold file paths
    file_paths = []

    # Save uploaded files
    files = request.files.getlist('files')
    for file in files:
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)  # Save file to the directory
            file_paths.append(file_path)  # Add file path to the list

    # Create a document to insert into MongoDB
    document = {
        'name': name,
        'surname': surname,
        'phone': phone,
        'email': email,
        'message': message,
        'jobId': job_id,  # Store the jobId in the document
        'files': file_paths
    }

    # Insert the data into MongoDB
    result = collection.insert_one(document)
    
    if result.inserted_id:
        return jsonify({"message": "Application submitted successfully!", "id": str(result.inserted_id)}), 201
    else:
        return jsonify({"error": "Failed to submit application."}), 500 

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    existing_user = users.find_one({'email': data['email']})

    if existing_user:
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    user = {
        'email': data['email'],
        'password': hashed_password,
        'user_type': data['userType'],
        'name': data.get('name'),
        'surname': data.get('surname'),
        'org_name': data.get('orgName'),
        'reg_number': data.get('regNumber'),
        'location': data.get('location'),
        'email_confirmed': False  # Initially set to False
    }

    users.insert_one(user)

    # Generate a 6-digit OTP
    otp = ''.join(random.choices(string.digits, k=6))
    otp_store[data['email']] = otp  # Store OTP for the user temporarily

    # Send the OTP via email
    msg = Message("Your OTP Code", sender="work4uauto@gmail.com", recipients=[data['email']])
    msg.body = f"Your OTP code is: {otp}. Please enter this code to complete your registration."
    
    try:
        mail.send(msg)
    except Exception as e:
        print("Failed to send email:", e)
        return jsonify({'message': 'User registered, but failed to send OTP email.'}), 500

    response = make_response(jsonify({'message': 'User registered successfully. Please check your email for the OTP.', 'email': data['email']}), 201)
    return response

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data['email']
    otp = data['otp']

    # Check if the OTP is correct
    if otp_store.get(email) == otp:
        # Mark email as confirmed
        users.update_one({'email': email}, {'$set': {'email_confirmed': True}})
        del otp_store[email]  # Remove OTP after verification
        return jsonify({'message': 'Email confirmed successfully! You can now log in.'}), 200
    else:
        return jsonify({'message': 'Invalid OTP. Please try again.'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({'email': data['email']})

    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        if not user.get('email_confirmed', False):
            return jsonify({'message': 'Please confirm your email before logging in.'}), 403
        
        token = jwt.encode({'email': data['email'], 'exp': datetime.utcnow() + timedelta(days=1)}, app.secret_key, algorithm='HS256')
        tokenlist.insert_one({'token': token})
        # Create a response with the token
        response = make_response(jsonify({'message': 'Login successful', 'email': data['email']}))
        response.set_cookie('token', token, httponly=True, samesite='Strict')
        session['user_id'] = str(user['_id'])

        return response
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/user-applications', methods=['GET'])
def get_user_applications():
    # Get user email from headers
    user_email = request.headers.get('userEmail')
    print(f"Received request with userEmail: {user_email}")
    
    if not user_email:
        print("No userEmail provided in the request headers.")
        return jsonify({"error": "User email not provided."}), 400
    
    # Fetch applications for the user
    user_applications = list(collection.find({"email": user_email}, {"_id": 0}))
    print(f"Applications found for user: {user_applications}")

    applications_with_job_details = []
    
    for application in user_applications:
        job_id = application.get("jobId")
        print(f"Fetching job details for jobId: {job_id}")

        # Fetch job details from JobAdvert where `id` matches `jobId`
        job_advert = jobAdvert.find_one({"id": int(job_id)}, {"_id": 0, "Company_name": 1, "Job_title": 1, "salary": 1})

        if job_advert:
            print(f"Job details found for jobId {job_id}: {job_advert}")
            # Merge job details into the application document
            application["Company_name"] = job_advert.get("Company_name")
            application["Job_title"] = job_advert.get("Job_title")
            application["salary"] = job_advert.get("salary")
        else:
            print(f"No job details found for jobId: {job_id}")

        applications_with_job_details.append(application)
    
    print(f"Final applications data sent to frontend: {applications_with_job_details}")
    return jsonify(applications_with_job_details), 200


@app.route('/delete-account', methods=['POST'])
def delete_account():
    user_id = session.get('user_id')  # Get user ID from session
    data = request.get_json()
    password = data.get('password')
    user = users.find_one({'_id': ObjectId(user_id)})

    # Check if user exists and validate password
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):  # No encoding on user['password']
        # Delete user account
        users.delete_one({'_id': ObjectId(user_id)})
        
        # Log the user out after deletion
        logout()
        
        return jsonify({'message': 'Account successfully deleted'}), 200
    else:
        return jsonify({'error': 'Invalid password'}), 403

@app.route('/jobs/<id>', methods=['GET', 'DELETE'])
def manage_product_by_id(id):
    if request.method == 'GET':
        query = {"id": int(id)}
        result = jobAdvert.find_one(query)
        return json_util.dumps(result)
    
    if request.method == 'DELETE':
        jobAdvert.delete_one({"id": int(id)})
        return '', 204

@app.route('/jobs', methods=['GET', 'POST'])
def get_jobs():
    if request.method == 'GET':
        filter_criteria = {}

        # Capture filtering parameters
        worktype = request.args.get('worktype')
        profession = request.args.get('profession')
        typeOfwork = request.args.get('typeOfwork')
        city = request.args.get('city')
        schedule = request.args.get('schedule')
        workTime = request.args.get('workTime')
        sort_order = request.args.get('sort')  # Capture the sort parameter (newest or oldest)

        # Apply filters if present
        if worktype:
            filter_criteria['worktype'] = {'$in': worktype.split(',')}
        if profession:
            filter_criteria['profession'] = {'$in': profession.split(',')}
        if typeOfwork:
            filter_criteria['typeOfwork'] = {'$in': typeOfwork.split(',')}
        if city:
            filter_criteria['city'] = {'$in': city.split(',')}
        if schedule:
            filter_criteria['schedule'] = {'$in': schedule.split(',')}
        if workTime:
            filter_criteria['workTime'] = {'$in': workTime.split(',')}

        print("Filter criteria received:", filter_criteria)  # Debug

        # Determine sort order (newest or oldest)
        sort_direction = -1 if sort_order == 'newest' else 1  # -1 for descending, 1 for ascending
        result = jobAdvert.find(filter_criteria).sort('date', sort_direction)  # Sort by 'date'

        jobs = list(result)
        return json_util.dumps(jobs)
    
    elif request.method == 'POST':
        product_data = request.json
        if not product_data.get('id'):
            product_data['id'] = random.randint(100000, 1000000)
        jobAdvert.insert_one(product_data)
        return json_util.dumps(product_data), 201


@app.route('/create_job_advert', methods=['POST'])
def create_job_advert():
    if request.method == 'POST':
        product_data = request.json
        
        # Add a creation date if it's not provided
        if not product_data.get('date'):
            product_data['date'] = datetime.utcnow()

        if not product_data.get('id'):
            product_data['id'] = random.randint(100000, 1000000)
        
        jobAdvert.insert_one(product_data)
        return json_util.dumps(product_data), 201


@app.route('/logout', methods=['POST'])
def logout():
    token = request.cookies.get('token')
    if token:
        tokenlist.delete_one({'token': token})
        response = make_response(jsonify({'message': 'Logged out successfully'}), 200)
        response.delete_cookie('token')
        return response
    else:
        return jsonify({'message': 'Token missing'}), 400

@app.route('/verify-token', methods=['GET'])
def verify_token():
    token = request.cookies.get('token')
    if token:
        try:
            data = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            if tokenlist.find_one({'token': token}):
                return jsonify({'message': 'Token is valid'})
            else:
                return jsonify({'message': 'Token is invalid!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 401
    else:
        return jsonify({'message': 'Token is missing!'}), 401

@app.route('/update_profile_image', methods=['POST'])
def update_profile_image():
    data = request.get_json()
    email = data.get('email')
    profile_image_url = data.get('profileImageUrl')

    if not email or not profile_image_url:
        return jsonify({'message': 'Email and profile image URL are required'}), 400

    user = users.find_one({'email': email})

    if not user:
        return jsonify({'message': 'User not found'}), 404

    users.update_one({'email': email}, {'$set': {'profileImageUrl': profile_image_url}})

    return jsonify({'message': 'Profile image updated successfully'}), 200

@app.route('/user', methods=['POST'])  # For "Profile" page
def get_user_by_email():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')

        if not email:
            return jsonify({"error": "Email is required"}), 400

        query = {"email": email}
        result = users.find_one(query)

        if result:
            return json_util.dumps(result), 200
        else:
            return jsonify({"error": "User not found"}), 404
 

@app.route('/add-favorite', methods=['POST'])
def add_favorite():
    data = request.get_json()
    user_email = data.get('email')
    job_id = data.get('job_id')

    if not user_email or not job_id:
        return jsonify({"error": "Email and Job ID are required"}), 400

    favorite = {
        'user_email': user_email,
        'job_id': job_id
    }

    # Add the favorite to the Favorites collection
    db.Favorites.insert_one(favorite)
    return jsonify({"message": "Favorite added successfully"}), 201

@app.route('/favourites', methods=['POST', 'OPTIONS'])
def get_favorites():
    if request.method == 'OPTIONS':
        return _build_cors_prelight_response()
    
    data = request.get_json()
    user_email = data.get('userEmail')

    if not user_email:
        return jsonify({"error": "Email is required"}), 400

    # Find all favorite job IDs for the user
    favorites = db.Favorites.find({'user_email': user_email})
    job_ids = [favorite['job_id'] for favorite in favorites]

    # Find job details for each favorite job ID
    favorite_jobs = list(db.JobAdvert.find({'_id': {'$in': [ObjectId(job_id) for job_id in job_ids]}}))

    return json_util.dumps(favorite_jobs), 200

def _build_cors_prelight_response():
    response = make_response()
    origin = request.headers.get('Origin')
    if origin in ["http://localhost:5174", "http://localhost:5173", "http://localhost:5000"]:
        response.headers.add("Access-Control-Allow-Origin", origin)  # Dynamically set allowed origin
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response

@app.route('/delete-favorite', methods=['POST'])
def delete_favorite():
    data = request.get_json()
    user_email = data.get('userEmail')
    job_id = data.get('jobId')

    if not user_email or not job_id:
        return jsonify({"error": "Email and Job ID are required"}), 400

    favorite = {
        'user_email': user_email,
        'job_id': job_id
    }

    # Add the favorite to the Favorites collection
    db.Favorites.delete_one(favorite)
    return jsonify({"message": "Favorite deleted successfully"}), 201

@app.route('/password_change', methods=['POST'])
def password_change():
    data = request.get_json()
    email = data.get('email')
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    
    if not email or not old_password or not new_password:
        return jsonify({'message': 'Email, old password, and new password are required'}), 400

    user = users.find_one({'email': email})

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if bcrypt.checkpw(old_password.encode('utf-8'), user['password']):
        hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        users.update_one({'email': email}, {'$set': {'password': hashed_new_password}})
        return jsonify({'message': 'Password updated successfully'}), 200
    else:
        return jsonify({'message': 'Old password is incorrect'}), 401

@app.route('/my_adverts', methods=['POST'])
def my_adverts():
    data = request.get_json()
    email = data.get('email')

    result = list(jobAdvert.find({"email": email}))

    return json_util.dumps(result), 200

@app.route('/update_name', methods=['POST'])
def update_name():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        surname = data.get('surname')

        # Validate input
        if not email or not name or not surname:
            return jsonify({'error': 'Email, name, and surname are required.'}), 400

        user = users.find_one({'email': email})

        if not user:
            return jsonify({'error': 'User not found.'}), 404

        # Update the user's name and surname
        users.update_one(
            {'email': email},
            {'$set': {'name': name, 'surname': surname}}
        )

        return jsonify({'message': 'Name and surname updated successfully.'}), 200


@app.route('/applicants/<job_id>', methods=['GET'])
def get_applicants(job_id):
    user_email = request.headers.get('userEmail')
    print(f"Received job ID: {job_id}")  # Log the job_id for debugging

    # Query for the job advert using the job_id
    job_advert = jobAdvert.find_one({"id": int(job_id)})  # Expect job_id to be an integer

    if not job_advert:
        print(f"Job advert with ID {job_id} not found.")
        return jsonify({"error": "Job advert not found."}), 404

    # Check if the user is authorized
    if job_advert['email'] != user_email:
        return jsonify({"error": "Unauthorized access. You are not the creator of this job advert."}), 403

    # Fetch applicants related to this job
    applicants = list(db.applications.find({"jobId": job_id}, {"_id": 0}))

    if applicants:
        return jsonify(applicants), 200
    else:
        return jsonify([]), 200
    

def delete_old_jobs():
    # Get the current date and calculate the cutoff date (6 months ago)
    cutoff_date = datetime.now() - timedelta(days=6 * 30)  
    # Delete documents older than 6 months
    result = jobAdvert.delete_many({"date": {"$lt": cutoff_date}})
    print(f"Deleted {result.deleted_count} job advertisements older than 6 months.")

def delete_all_tokens():
    # Delete all documents in the collection
    result = tokenlist.delete_many({})
    print(f"Deleted {result.deleted_count} Tokens")

# Run the delete function within the application context
with app.app_context():
    delete_old_jobs()
    delete_all_tokens()


if __name__ == "__main__":
    app.run(debug=True)
