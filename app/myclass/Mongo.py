import os
from pymongo import MongoClient

class MongoConnect():

    '''Docstring for the class'''

    username = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']
    db_name = os.environ['DB_NAME']

    def __init__(self):
        pass

    def connect(self):
        client = MongoClient \
            (f'mongodb+srv://{self.username}:{self.password} \
            @fii-api.gnuy4.mongodb.net/{self.db_name}?retryWrites=true&w=majority')
        db_conn = client.dev.daily_info
        return db_conn