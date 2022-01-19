from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_loc'] = request.form['dojo_loc']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']

    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')


if __name__=="__main__":
    app.run(debug = True)