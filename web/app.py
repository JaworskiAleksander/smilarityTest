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


def UserExists(username):
    result = users.find({
        'Username': username
    })[0]
    if result:
        return True
    else:
        return False


class Register(Resource):
    def post(self):
        # Step 1 - get the posted data
        postedData = request.get_json()

        # Step 2 - get username and password
        username = postedData['username']
        password = postedData['password']

        # Step 3 - validate user credentials
        if UserExists(username):
            retJSON = {
                'status':   301,
                'message':  'invalid username'
            }
            return jsonify(retJSON)

        # Step 4 - store hashed password, because we're registering a new user
        hashed_pw = bcrypt.hashed_pw(
            password.encode('utf-8'), bcrypt.gensalt())

        # Step 5 - input username and hashed password into database
        insertResult = users.insertOne({
            'Username':     username,
            'Password':     hashed_pw,
            'Tokens':       10
        })
