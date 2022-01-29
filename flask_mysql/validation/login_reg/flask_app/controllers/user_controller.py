from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Must be logged in to access dashboard.')
        return redirect('/')

    data = {
        'id' : session['user_id']
    }

    user = User.get_user_by_id(data)

    return render_template('dashboard.html', user=user)

@app.route('/register', methods=['POST'])
def register_user():
    # validate first
    if not User.validate_user(request.form):
        return redirect('/')

    # will need to modify data to account for password, pw_confirm, and pw_hash
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'pw_hash' : bcrypt.generate_password_hash(request.form['password'])
    }

    new_user_id = User.create_user(data)

    session['user_id'] = new_user_id

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email' : request.form['email'],
        'password' : request.form['password']
    }

    if not User.validate_login(data):
        return redirect('/')

    session['user_id'] = User.get_user_by_email(data).id

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')