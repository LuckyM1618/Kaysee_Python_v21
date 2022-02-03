from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    # only adding one, since redirect adds one as well
    session['count'] += 1

    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)