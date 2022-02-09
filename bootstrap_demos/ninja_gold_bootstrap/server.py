from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

messages = []

@app.route('/')
def index():
    if 'current_gold' not in session:
        session['current_gold'] = 0
    return render_template('index.html', messages=messages)

@app.route('/process_money', methods=['POST'])
def process_money():
    # Farm
    # earns 10 - 20 gold
    if request.form['loc'] == 'farm':
        farm_payout = random.randint(10, 20)
        session['current_gold'] += farm_payout
        messages.append(f'<p>You gained {farm_payout} gold from the farm!</p>')

    # Cave
    # earns 5 - 10 gold
    if request.form['loc']  == 'cave':
        session['current_gold'] = 20

    # House
    # earns 2 - 5 gold
    if request.form['loc']  == 'house':
        session['current_gold'] = 30

    # Casino
    # earns/takes 0 - 50 gold
    if request.form['loc']  == 'casino':
        session['current_gold'] = 40


    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    messages.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug = True)