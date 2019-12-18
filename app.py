import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'PlantPal'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plants')
def view_plants():
    return render_template('plants.html', plants=mongo.db.plants.find())

@app.route('/plant/new', methods=['GET', 'POST'])
def add_plant():
    if request.method=='POST':
        plants  = mongo.db.plants
        plants.insert_one(request.form.to_dict())
        return redirect(url_for('view_plants'))
    return render_template("add_plant.html")

@app.route('/plants/<plant_id>', methods=['GET'])
def view_plant(plant_id):
    plant=mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template('plant.html', plant=plant)
    
@app.route('/create_account')
def create_account():
    return render_template("create_account.html")
    
    
@app.route('/insert_user', methods=['POST'])
def insert_user():
    users  = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('view_plant'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)