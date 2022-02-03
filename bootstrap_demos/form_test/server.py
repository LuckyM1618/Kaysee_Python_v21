from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    print("Wake up, Neo", flush=True)
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user():
    print('Knock, knock, Neo')
    print(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug = True)