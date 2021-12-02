from boto3 import client
from pymongo import MongoClient
import os

class MongoConnect():
    username = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']
    db_name = os.environ['DB_NAME']

    def __init__(self):
        pass

    def connect(self):
        client = MongoClient('mongodb+srv://{}:{}@fii-api.gnuy4.mongodb.net/{}?retryWrites=true&w=majority'.format(self.username,self.password,self.db_name))
        db = client.dev.daily_info
        return db


