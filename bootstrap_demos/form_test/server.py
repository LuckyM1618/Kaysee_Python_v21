from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    print("Wake up, Neo", flush=True)
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    print('Knock, knock, Neo')
    print(request.form)
    session['user'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__=="__main__":
    app.run(debug = True)