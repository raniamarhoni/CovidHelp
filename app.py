import os
import pymongo
from flask import Flask
from flask_pymongo import flask_pymongo
from bson.objectid import ObjectId

app = Flask(__name__)


if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "covidhelp"
COLLECTION = "users"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MONGODB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()


for doc in documents:
    print(doc)


@app.route('/')
def hello():
    return "Hello World ... again! "


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
