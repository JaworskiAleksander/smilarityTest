from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy


# initialize api
app = Flask(__name__)
api = Api(app)

# connect to mongoDB
client = MongoClient('mongodb://db:27017')
db = client['SimilarityDB']
users = db['Users']


def userExists(username):
    # result = users.find({
    #     'Username': username
    # }).count()
    # if result == 0:
    #     return True
    # else:
    #     return False

    # sleek
    return bool(users.find({
        'Username': username
    }).count())


def verifyPassword(username, password):
    pass


def countTokens(username):
    pass


class Register(Resource):
    def post(self):
        # Step 1 - get the posted data
        postedData = request.get_json()

        # Step 2 - get username and password
        username = postedData['username']
        password = postedData['password']

        # Step 3 - validate user credentials
        if userExists(username):
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

        # Step 6 - return message after successfully registering user
        retJSON = {
            'status':       200,
            'message':      'Sign up went successfully, congratulations!'
        }

        return jsonify(retJSON)


class Detect(Resource):
    def post(self):
        # Step 1 - get the posted data
        postedData = request.get_json()

        # Step 2 - decompose data sent by user
        username = postedData['username']
        password = postedData['password']
        text1 = postedData['text1']
        text2 = postedData['text2']

        # Step 3 - verify user credentials
        # Step 3A - username
        if not userExists(username):
            retJSON = {
                'status':   301,
                'message':  'invalid username'
            }

            return jsonify(retJSON)

        # Step 3B - password
        correct_password = verifyPassword(username, password)

        if not correct_password:
            retJSON = {
                'status':   302,
                'message':  'invalid password'
            }

            return jsonify(retJSON)

        # Step 3C - tokens
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJSON = {
                'status':   303,
                'message':  'not enough tokens, please refill'
            }

            return jsonify(retJSON)

        # Step 4 - calculate the edit distance -> spaCy to the rescue!
        nlp = spacy.load('en_core_web_sm')

        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        # Step 5 - subtract 1 token
        tokensLeft = users.find({
            'Username': username
        })[0]['Tokens']

        tokensLeft -= 1

        users.update(
            {
                'Username': username
            },
            {
                '$set': {
                    'Tokens':   tokensLeft
                }
            })

        # Step 6 - return calculated similarity ratio
        retJSON = {
            'status':       200,
            'similarity':   ratio,
            'message':      'Similiarity score calculated successfully',
            'tokens':       f'{tokensLeft} tokens remaining at {username} account'

        }

        return jsonify(retJSON)
