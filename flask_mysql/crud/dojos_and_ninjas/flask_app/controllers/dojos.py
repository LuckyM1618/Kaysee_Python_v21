from flask_app import app
from venv import create
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all_dojos_with_ninjas()

    return render_template('index.html', dojos=dojos)
