import os
from flask import  Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook-book'
app.config["MONGO_URI"] ='mongodb://Mel28:AlexGauci333@ds131601.mlab.com:31601/cook-book'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
        tasks=mongo.db.recipes.find())

@app.route('/')
def hello():
    return 'Hello world....third time lucky!'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)