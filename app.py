import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'PlantPal'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://sianjade:druidfan95@myfirstcluster-0vxhc.mongodb.net/PlantPal?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')

@app.route('/add_plant')
def hello():
    return render_template("add_plant.html", plant=mongo.db.plants.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)