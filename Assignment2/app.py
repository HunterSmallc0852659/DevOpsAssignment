# pip install flask
# pip install python-dotenv

from flask import Flask, render_template
from dotenv import load_dotenv
# pip install pymongo
from pymongo import MongoClient

import os
load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')


#creates mongodb client
client = MongoClient(
    "mongodb+srv://"+ MONGODB_USERNAME +":"+ MONGODB_PASSWORD +"@cluster0.j7lmr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#access database from client
db = client.shop_db
products_collection = db.products

#add data mongo db; insert_many(), insert_one()
#list of json or one json


mock_data = [{"name": "product 1",
              "tag": "new",
              "price": 10,
              "img_path": "/static/images/chef_3.webp"},
             {"name": "product 2",
              "tag": "new",
              "price": 10.02,
              "img_path": "/static/images/chef_4.jpg"}
             ]
#comment out to stop inserting data
#products_collection.insert_many(mock_data)

#create app instance
flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/products")
def products():
    product = list(products_collection.find())
    return render_template("products.html", products=product)



flask_app.run(host="0.0.0.0", port=5000)