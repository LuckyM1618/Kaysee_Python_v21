from flask_app import app
from venv import create
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : int(request.form['age']),
        'dojo_id' : request.form['dojo_id']
    }

    Ninja.save(data)

    dojo_id = data['dojo_id']

    return redirect(f'/dojos/{dojo_id}')