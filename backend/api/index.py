from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util, ObjectId

app = Flask(__name__)
CORS(app)  # This should be sufficient, but if needed, you can specify origins

client = MongoClient("mongodb+srv://23_DpMParums:J3imyzZW2lCp3mNx@uwork.wlvyybo.mongodb.net/?retryWrites=true&w=majority&appName=Uwork")

db = client.Uwork
JobAdvert = db.JobAdvert

@app.route('/jobs', methods=['GET'])
def get_jobs():
    orders_list = list(JobAdvert.find())
    return json_util.dumps(orders_list)

if __name__ == '__main__':
    app.run(debug=True)