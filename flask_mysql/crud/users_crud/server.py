from venv import create
from flask import Flask, render_template, redirect, request
# import the class from user.py
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()

    return render_template("read_all.html", users=users)

@app.route('/new_user')
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
    User.save(data)

    # Don't forget to redirect after saving to the database.
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)