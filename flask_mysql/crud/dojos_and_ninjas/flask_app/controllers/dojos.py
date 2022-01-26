from flask_app import app
from venv import create
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all_dojos()

    return render_template('all_dojos.html', dojos=dojos)

@app.route('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }

    dojo = Dojo.get_one_dojo_with_ninjas(data)

    return render_template('one_dojo.html', dojo=dojo)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }

    Dojo.save(data)

    return redirect('/dojos')

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all_dojos()

    return render_template('create_ninja.html', dojos=dojos)


