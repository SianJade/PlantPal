import os
# import env
import datetime
from flask import Flask, render_template, redirect, request, url_for, session, escape, flash
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


""" App routes """
@app.route('/')
@app.route('/index')
def home():
    """App route for index.html/home page"""
    return render_template('index.html')


@app.route('/plants')
def view_plants():
    """ View alphabetical list of each individual plant in the database """
    return render_template('plants.html', plants=mongo.db.plants.find().sort('latin_name', pymongo.ASCENDING))


@app.route('/plant/new', methods=['GET', 'POST'])
def add_plant():
    """ Check if the user is logged in """
    if 'user_id' in session:
        """ If they are, they may add a new plant to the database """
        if request.method=='POST':
            form = request.form.to_dict()
            """ Check if a plant with the inputted latin name already exists in the database """
            plant_in_db = mongo.db.plants.find_one({'latin_name': form['latin_name']})
            if plant_in_db:
                """ If the plant does already exist in the database, inform the user """
                flash(u'A page already exists for this plant', 'plant_exists')
            else:
                """ If the plant does not already exist in the databse, allow the plant info to be saved to the database """
                form["created_by"] = session['username']
                plant_id = mongo.db.plants.insert_one(form)
                plant = mongo.db.plants.find_one({"_id" : ObjectId(plant_id.inserted_id)})
                """ Once plant has been successfully added to databse, redirect user to page for newly created plant """
                return render_template('plant.html', plant=plant)
        return render_template("add_plant.html")
    else:
        """ If the user is not logged in, redirect them to the login page """
        flash(u'You must be logged in', 'login')
        return render_template('login.html')


@app.route('/plants/<plant_id>', methods=['GET'])
def view_plant(plant_id):
    """ View one specific plant from the databse and all its details """
    plant=mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template('plant.html', plant=plant)


@app.route('/plants/edit/<plant_id>')
def edit_plant(plant_id):
    """ Check if the user is logged in """
    if 'username' in session:
        """ If they are, allow the user to edit plant details """
        plant = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})
        return render_template('edit_plant.html', plant=plant)
    else:
        """ If the user is not logged in, redirect them to the login page """
        flash(u'You must be logged in', 'login')
        return render_template('login.html')


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
        'plant_image': request.form.get('plant_image')
    })
    """ Once updated, redirect user to the updated plant's info page """
    return redirect(url_for('view_plant', plant_id=plant_id))


@app.route('/plants/delete_plant/<plant_id>')
def delete_plant(plant_id):
    """ Check if the user is logged in """
    if 'username' in session:
        """ If they are, allow the user to delete a plant and its details """
        plant = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})
        if plant["created_by"] == session['username']:
            mongo.db.plants.remove({'_id': ObjectId(plant_id)})
            return redirect(url_for('view_plants'))
        else:
            flash(u'Only the initial creator of the page for this plant has permission to delete it', 'delete')
            return redirect(url_for('view_plant', plant_id=plant_id)) 
    else:
        """ If the user is not logged in, redirect them to the login page """
        flash(u'You must be logged in', 'login')
        return render_template('login.html')


@app.route('/plants/genera')
def genera():
    """
    Browse alphabetical list of all plant genera, distinct() is used to ensure each genus is only
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
        user_in_db = mongo.db.users.find_one({'username': form['username']})
        if user_in_db:
            flash(u'An account already exists for this username - please pick a new username', 'username_exists')
        else:
            user_password = generate_password_hash(form['password1'])
            user_id = mongo.db.users.insert_one({
                'first_name': form['first_name'],
                'last_name': form['last_name'],
                'email': form['email'],
                'username': form['username'],
                'password': user_password
            })
            user = mongo.db.users.find_one({"_id" : ObjectId(user_id.inserted_id)})
            session['user_id'] = str(user_id.inserted_id)
            return render_template('user.html', user=user)
    return render_template('create_account.html')


@app.route('/user/edit/<user_id>')
def edit_user(user_id):
    """
    Allows a user to edit their profile
    """
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    return render_template('edit_account.html', user=user)


@app.route('/user/update_user/<user_id>', methods=["POST"])
def update_user(user_id):
    """
    Update the details of a user, the form is pre-filled with the all of the details for the
    user as they are currently stored in the database. 
    """
    user = mongo.db.users
    user.update({'_id': ObjectId(user_id)},
    {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
    })
    """ Once updated, redirect user to the updated user's profile page """
    return redirect(url_for('profile', user_id=user_id))


@app.route('/user/delete_user/<user_id>')
def delete_account(user_id):
    """
    Allow the user to delete their profile
    """
    mongo.db.users.find_one({'_id': ObjectId(user_id)})
    mongo.db.users.remove({'_id': ObjectId(user_id)})
    session.clear()
    flash(u'Account deleted successfully', 'account_deleted')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET'])
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
            session['user_id'] = str(user_in_db['_id'])
            return redirect(url_for('profile', user_id=user_in_db['_id']))
        else:
            flash(u'Wrong username or password', 'wrong')
            return redirect(url_for('login'))
    else:
        flash(u'An account does not exist for this username', 'user_does_not_exist') 
        return redirect(url_for('login'))

@app.route('/user/<user_id>', methods=['GET'])
def profile(user_id):
    """ Allows the user to see their profile details """
    return render_template('user.html', user=mongo.db.users.find_one({"_id": ObjectId(user_id)}), user_id=user_id)


@app.route('/logout')
def logout():
    """ Log out of account by clearing the session then redirect to index.html"""
    session.clear()
    flash(u'Logout successful', 'logout_success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)