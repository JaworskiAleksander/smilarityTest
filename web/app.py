from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

# initialize api
app = Flask(__name__)
api = Api(app)

# connect to mongoDB
