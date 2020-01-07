import os
import env
import datetime
from flask import Flask, render_template, redirect, request, url_for, session, escape, flash
from flask_login import LoginManager, UserMixin, login_required
from flask_pymongo import PyMongo
import pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


""" App config """
app = Flask(__name__)
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
    """App route for index.html/home page"""
    return render_template('index.html')


@app.route('/plants')
def view_plants():
    """ View all individual plants in the database """
    return render_template('plants.html', plants=mongo.db.plants.find().sort('latin_name', pymongo.ASCENDING))


@app.route('/plant/new', methods=['GET', 'POST'])
def add_plant():
    """ Add a new plant to the database """
    if 'username' in session:
        if request.method=='POST':
            plants  = mongo.db.plants
            form = request.form.to_dict()
            form["created_at"] = datetime.datetime.now()
            form["created_by"] = [session['username']]
            form["updated_at"] = datetime.datetime.now()
            plants.insert_one(form)
            return redirect(url_for('view_plants'))
        return render_template("add_plant.html")
    else:
        flash('You must be logged in to view this page')
        return render_template('login.html')


@app.route('/plants/<plant_id>', methods=['GET'])
def view_plant(plant_id):
    """ View one specific plant from the databse and all its details """
    plant=mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template('plant.html', plant=plant)


@app.route('/plants/edit/<plant_id>')
def edit_plant(plant_id):
    """ App route for the edit plant page """
    plant = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})
    return render_template('edit_plant.html', plant=plant)


@app.route('/plants/update_plant/<plant_id>', methods=["POST"])
def update_plant(plant_id):
    """
    Update the details of a plant, the form is pre-filled with the all of the details for the
    plant as it is currently stored in the database. 
    """
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
        'additional_notes': request.form.get('additional_notes'),
        'updated_at': datetime.datetime.now()
        # 'created_by': 
    })
    return redirect(url_for('view_plant', plant_id=plant_id))



@app.route('/plants/delete_plant/<plant_id>')
def delete_plant(plant_id):
    """ Delete a single plant and its detils from the database """
    mongo.db.plants.remove({'_id': ObjectId(plant_id)})
    return redirect(url_for('view_plants'))


@app.route('/plants/genera')
def genera():
    """
    Browse all plant genera, distinct() is used to ensure each genus is only
    listed on the page once, otherwise multiple of the same genus name are displayed
    if there is more than one plant of that genus in the database 
    """
    genera = mongo.db.plants.distinct("genus")
    genera.sort()
    return render_template('genera.html', genera=genera)


@app.route('/plants/genus/<genus_name>')
def genus(genus_name):
    """ See all plants within the genus selected by the user on genera.html """
    return render_template('genus.html', plants=mongo.db.plants.find({"genus": genus_name}), genus_name=genus_name)
    


@app.route('/get_search', methods=['POST'])
def get_search():
    """ 
    Search for a plant by latin or common name, soil type, family, order, genus, indoor/outdoor, 
    lighting preferences, and watering frequency 
    """
    query = request.form['search_text']
    results = mongo.db.plants.find({'$text':{'$search': query}})
    return render_template('search_results.html', results=results, query=query)



@app.route('/user/new', methods=['GET', 'POST'])
def create_account():
    """ 
    Create a new user account and return user.html showing the user's 
    new account details uppon successful account creation
    """
    if request.method=='POST':
        form = request.form.to_dict()
        user_password = generate_password_hash(form['password'])
        user_id = mongo.db.users.insert_one({
            'first_name': form['first_name'],
            'last_name': form['last_name'],
            'email': form['email'],
            'username': form['username'],
            'password': user_password
        })
        user = mongo.db.users.find_one({"_id" : ObjectId(user_id.inserted_id)})
        return render_template('user.html', user=user)
    return render_template('create_account.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    """ 
    Check if the username is already in the session and redirect them to their profile if so
    If the user is not in the session, redirect them to the login page
    """
    return render_template("login.html")


@app.route('/authentication', methods=['POST'])
def authentication():
    """ 
    Authenticate username and password by checking the inputted username matches 
    the inputted username stored in the users collection of the db, and that the 
    inputted password matches the password stored in the db, and then that the 
    password is the correct password for the inputted username. If the username
    and password do not match or are incorrect, then the user will see a message 
    informing them of this and the login page will refresh. If the inputted username
    does not exist in the database at all, the user will see a message informing
    them that an account does not exist for the user
    """
    form = request.form.to_dict()
    user_in_db = mongo.db.users.find_one({'username': form['username']})
    if user_in_db:
        if check_password_hash(user_in_db['password'], form['password']):
            session['username'] = form['username']
            return redirect(url_for('profile', user_id=user_in_db['_id']))
        else:
            session['message'] = "Wrong username or password"
            return redirect(url_for('login'))
    else:
        session['message'] = "An account does not exist for this username" 
        return redirect(url_for('login'))

@app.route('/user/<user_id>', methods=['GET'])
def profile(user_id):
    """ Allows the user to see their profile details """
    return render_template('user.html', user=mongo.db.users.find_one({"_id": ObjectId(user_id)}), user_id=user_id)


@app.route('/logout')
def logout():
    """ Log out of account by clearing the session then redirect to index.html"""
    session.clear()
    flash("Logout successful")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)