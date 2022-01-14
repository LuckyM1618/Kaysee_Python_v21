from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/<user_input>')
def dojo(user_input):
    return user_input

@app.route('/say/<string:name>')
def say_hi(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<string:user_str>')
def repeat(num, user_str):
    return user_str * num

if __name__=="__main__":
    app.run(debug=True)
