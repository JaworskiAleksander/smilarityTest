from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

# initialize api
app = Flask(__name__)
api = Api(app)

# connect to mongoDB
client = MongoClient('mongodb://db:27017')
db = client['SimilarityDB']
users = db['Users']


class Register(Resource):
    def post(self):
        # Step 1 - get the posted data
        postedData = request.get_json()

        # Step 2 - get username and password
        username = postedData['username']
        password = postedData['password']
