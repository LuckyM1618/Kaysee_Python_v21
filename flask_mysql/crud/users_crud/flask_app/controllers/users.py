from flask_app import app
from venv import create
from flask import render_template, redirect, request
# import the class from user.py
from flask_app.models.user import User

@app.route("/users")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()

    return render_template("read_all.html", users=users)

@app.route('/users/new')
def new_user():

    return render_template('create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    # We pass the data dictionary into the save method from the User class.
    user_id = User.save(data)

    # Don't forget to redirect after saving to the database.
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>')
def read_one(user_id):
    data = {
        'id_num' : user_id
    }

    user = User.get_one(data)

    return render_template('read_one.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id_num' : user_id
    }

    user = User.get_one(data)

    return render_template('edit.html', user=user)

@app.route('/update_user', methods=['POST'])
def update_user():
    data = {
        'id' : request.form['id'],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.update(data)

    user_id = request.form['id']
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id' : user_id
    }

    User.delete(data)

    return redirect('/users')