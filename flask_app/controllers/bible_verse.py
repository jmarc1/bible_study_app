from flask_app import app
from flask import flash,render_template,redirect,request

@app.route("/view_verse")
def add_verse():
    return render_template("viewEvent.html")

@app.route()