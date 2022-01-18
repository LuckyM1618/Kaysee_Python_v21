from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1

    return render_template('index.html')

@app.route('/add_two')
def add_two():
    # add one here, another added on redirect
    session['count'] += 1

    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()

    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)