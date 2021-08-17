from boto3 import client
from pymongo import MongoClient
import os

db_address = os.environ['DB_URL']
db_port = os.environ['DB_PORT']

client = MongoClient('mongodb://{}:{}'.format(db_address,db_port))

print(client.server_info)

db = client.daily_info

