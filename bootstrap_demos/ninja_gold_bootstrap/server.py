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
        messages.append(f'<p class=\"text-success\">You gained {farm_payout} gold from the farm!</p>')

    # Cave
    # earns 5 - 10 gold
    elif request.form['loc']  == 'cave':
        cave_payout = random.randint(5, 10)
        session['current_gold'] += cave_payout
        messages.append(f'<p class=\"text-success\">You gained {cave_payout} gold from the cave!</p>')

    # House
    # earns 2 - 5 gold
    elif request.form['loc']  == 'house':
        house_payout = random.randint(2, 5)
        session['current_gold'] += house_payout
        messages.append(f'<p class=\"text-success\">You gained {house_payout} gold from the house!</p>')

    # Casino
    # earns/takes 0 - 50 gold
    elif request.form['loc']  == 'casino':
        casino_payout = random.randint(-50, 50)
        if casino_payout >= 0:
            messages.append(f'<p class=\"text-success\">You won {casino_payout} gold at the casino!</p>')
        else:
            messages.append(f'<p class=\"text-danger\">You lost {casino_payout} gold at the casino...Ouch!</p>')

        session['current_gold'] += casino_payout


    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    messages.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug = True)