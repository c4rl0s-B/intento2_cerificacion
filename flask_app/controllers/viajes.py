from flask_app import app

from flask import render_template, redirect, flash
from flask_app.models.usuario import Usuario

@app.route('/dashboard')
def cine():
    return render_template('dashboard.html')