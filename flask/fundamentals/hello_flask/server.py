# Import Flask to allow us to create our app
from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase = "hello", times = 5)

@app.route('/success')
def success():
    return "Great Success!!!"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<user_id>')
def show_user_profile(username, user_id):
    print(username)
    print(user_id)
    return "Username: " + username + ", ID: " + user_id

@app.route('/lists')
def render_lists():
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]

    return render_template("lists.html", random_numbers = [3, 1, 5], students = student_info)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
