from flask import Flask, render_template, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    # generate new random number in session on game start


    return render_template('index.html')

@app.route('/process_guess', methods=['POST'])
def process_guess():
    # compare user's guess to answer stored in session


    # if guess is correct, set 'guessed_correctly' to True


    # else set 'guessed_correctly' to False


    pass

@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug = True)