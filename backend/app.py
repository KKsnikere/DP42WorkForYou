from flask import Flask, request, jsonify, session, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt
import jwt
import datetime
import os
import secrets
from bson import json_util, ObjectId
import json
import random
import string

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)
app.config['MONGO_URI'] = 'mongodb+srv://23_DpMParums:J3imyzZW2lCp3mNx@uwork.wlvyybo.mongodb.net/?retryWrites=true&w=majority&appName=Uwork'
mongo = PyMongo(app)
CORS(app, supports_credentials=True)

client = MongoClient(app.config['MONGO_URI'])
db = client.Uwork
jobAdvert = db.JobAdvert
users = db.Register
tokenlist = db.tokenlist

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

        worktype = request.args.get('worktype')
        profession = request.args.get('profession')
        typeOfwork = request.args.get('typeOfwork')
        city = request.args.get('city')
        schedule = request.args.get('schedule')
        workTime = request.args.get('workTime')

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

        print("Filter criteria received:", filter_criteria)  # Debug statement

        result = jobAdvert.find(filter_criteria)
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
        if not product_data.get('id'):
            product_data['id'] = random.randint(100000, 1000000)
        jobAdvert.insert_one(product_data)
        return json_util.dumps(product_data), 201

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
        'location': data.get('location')
    }
    users.insert_one(user)

    # Find the newly inserted user and extract the email
    new_user = users.find_one({'email': data['email']})
    email = new_user['email']

    token = jwt.encode({'email': data['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.secret_key, algorithm='HS256')
    tokenlist.insert_one({'token': token})

    response = make_response(jsonify({'message': 'User registered successfully', 'email': email}), 201)
    response.set_cookie('token', token, httponly=True, samesite='Strict')

    return response

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({'email': data['email']})

    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        token = jwt.encode({'email': data['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)}, app.secret_key, algorithm='HS256')
        tokenlist.insert_one({'token': token})

        response = make_response(jsonify({'message': 'Login successful', 'email': data['email']}))
        response.set_cookie('token', token, httponly=True, samesite='Strict')

        return response
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

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

@app.route('/user', methods=['POST']) #For "Profile" page
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
    user_email = data.get('userEmail')
    job_id = data.get('jobId')

    if not user_email or not job_id:
        return jsonify({"error": "Email and Job ID are required"}), 400

    favorite = {
        'user_email': user_email,
        'job_id': job_id
    }

    # Add the favorite to the Favorites collection
    db.Favorites.insert_one(favorite)
    return jsonify({"message": "Favorite added successfully"}), 201

@app.route('/favorites', methods=['POST'])
def get_favorites():
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


if __name__ == "__main__":
    app.run(debug=True)