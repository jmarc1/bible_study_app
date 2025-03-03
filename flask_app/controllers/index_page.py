from flask_app import app
from flask_app.models.events_model import bible_event
from flask import render_template,redirect,request,flash,session

@app.route('/')
def index():
    old_event = bible_event.get_event_users()
    return render_template('index.html',events = old_event)

@app.route('/past_event')
def past_event():
    old_event = bible_event.get_event_users()
    print(old_event)
    return render_template('past_event.html', events=old_event)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add_Event')
def add_Event():
    return render_template('create_event.html')

@app.route("/register")
def adduser():
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    if session['user'] == None:
        return redirect("/")
    get_inf =  bible_event.get_events()
    return render_template('dashboard.html', events =  get_inf)