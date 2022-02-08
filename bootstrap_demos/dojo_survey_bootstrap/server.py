from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "Sphinx of Black Quartz, Judge My Vow!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_results')
def show_results():
    pass


if __name__=="__main__":
    app.run(debug = True)