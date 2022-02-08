from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def show_results():
    session['name'] = request.form['name']
    session['dojo_loc'] = request.form['dojo_loc']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    
    return redirect('/results')

@app.route('/results')
def display_results():
    return render_template('results.html')


if __name__=="__main__":
    app.run(debug = True)