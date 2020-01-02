import os
import env
import datetime
from flask import Flask, render_template, redirect, request, url_for, session, escape, flash
from flask_login import LoginManager, UserMixin
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

""" App config """

app = Flask(__name__)

""" MongoDB config """

app.config["MONGO_DBNAME"] = 'PlantPal'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET")

mongo = PyMongo(app)

""" Login Manager """
login_manager = LoginManager()
login_manager.init_app(app)

""" App routes """
@app.route('/')

@app.route('/index')
def home():
    return render_template('index.html')

""" View all plants """
@app.route('/plants')
def view_plants():
    return render_template('plants.html', plants=mongo.db.plants.find())

""" Add a plant """
@app.route('/plant/new', methods=['GET', 'POST'])
def add_plant():
    if request.method=='POST':
        plants  = mongo.db.plants
        form = request.form.to_dict()
        form.created_at = datetime.datetime.now()
        #form.created_by = [session['username']]
        plants.insert_one(form)
        return redirect(url_for('view_plants'))
    return render_template("add_plant.html")

""" View a plant """
@app.route('/plants/<plant_id>', methods=['GET'])
def view_plant(plant_id):
    plant=mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template('plant.html', plant=plant)

""" Edit a plant """
@app.route('/plant/edit/<plant_id>', methods=['GET', 'POST'])
def edit_plant(plant_id):
    plant = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})
    if request.method=='POST':
        form = request.form.to_dict()
       # form.created_at = plant.created_at
       # form.updated_at = datetime.datetime.now()
        # form.created_by = input_created_by(plant.created_by, session['username'])
    return render_template('edit_plant.html', plant=plant)

@app.route('/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    plant = mongo.db.plants
    plant.update({'_id': ObjectId(plant_id)},
    {
        'latin_name': request.form.get('latin_name'),
        'common_name': request.form.get('common_name'),
        'order': request.form.get('order'),
        'family': request.form.get('family'),
        'genus': request.form.get('genus'),
        'preferred_lighting': request.form.get('preferred_lighting'),
        'indoor_outdoor': request.form.get('indoor_outdoor'),
        'water_frequency': request.form.get('water_frequency'),
        'soil_type': request.form.get('soil_type'),
        'additional_notes': request.form.get('additional_notes')
    })
    return redirect(url_for('view_plant'))

""" Browse by plant genus """
@app.route('/genus/<genus_name>')
def genus(genus_name):
    return render_template('genus.html', plants=mongo.db.plants.find({"genus": genus_name}))


""" Create an account """
@app.route('/user/new', methods=['GET', 'POST'])
def create_account():
    if request.method=='POST':
        form = request.form.to_dict()
        user_password = generate_password_hash(form['password'])
        user_id = mongo.db.users.insert_one({
            'first': form['first_name'],
            'last': form['last_name'],
            'email': form['email'],
            'username': form['username'],
            'password': user_password
        })
        user = mongo.db.users.find_one({"_id" : ObjectId(user_id.inserted_id)})
        return render_template('user.html', user=user_id)
    return render_template('create_account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash('Logged in as %s' % escape(session['username']))
        return redirect(url_for('home'))
    elif request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('login'))
    return render_template('login.html')
    

@app.route('/user/<user_id>', methods=['GET'])
def view_user(user_id):
    user=mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('user.html', user=user)
    
    
"""Log out of account"""
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been successfully logged out")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)