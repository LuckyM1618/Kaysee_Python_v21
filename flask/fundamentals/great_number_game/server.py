from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    
    return render_template('index.html')

@app.route('/process_guess', methods=["POST"])
def process_guess():
    guess = int(request.form['guess'])
    if guess == session['num']:
        session['last_guess'] = 'just right'
    elif guess < session['num']:
        session['last_guess'] = 'too low'
    elif guess > session['num']:
        session['last_guess'] = 'too high'
    else:
        session['last_guess'] = 'error'

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)