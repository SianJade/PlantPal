import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'PlantPal'
app.config["MONGO_URI"] = 'mongodb+srv://sianjade:druidfan95@myfirstcluster-0vxhc.mongodb.net/PlantPal?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/view_plant')
def view_plant():
    return render_template('plants.html', plants=mongo.db.plants.find())

@app.route('/add_plant')
def add_plant():
    return render_template("add_plant.html", add_plant=mongo.db.add_plant.find())

@app.route('/insert_plant', methods=['POST'])
def insert_plant():
    plants  = mongo.db.plants
    plants.insert_one(request.form.to_dict())
    return redirect(url_for('view_plant'))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)