from boto3 import client
from pymongo import MongoClient
import os

db_address = os.environ['DB_URL']
db_port = os.environ['DB_PORT']

# username = os.environ['DB_USERNAME']
# password = os.environ['DB_PASSWORD']
# name = os.environ['DB_NAME']

client = MongoClient('mongodb://{}:{}'.format(db_address,db_port))
# client = MongoClient('mongodb+srv://{}:{}@fii-api.gnuy4.mongodb.net/{}?retryWrites=true&w=majority'.format(username,password,name))


print(client.server_info)

db = client.daily_info




# client = pymongo.MongoClient("mongodb+srv://<username>:<password>@fii-api.gnuy4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test
