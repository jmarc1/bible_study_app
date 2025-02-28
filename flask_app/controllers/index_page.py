from flask_app import app
from flask import render_template,redirect,request,flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_Event')
def add_Event():
    return render_template('create_event.html')

@app.route("/register")
def adduser():
    return render_template("register.html")