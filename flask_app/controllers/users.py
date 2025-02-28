from flask_app import app
from flask import flash,request,render_template,redirect

@app.route('/add_user', methods=['POST'])
def add_user():
    data={
        "first_name":request.form['first_name'],
        "last_name":request.form["last_name"],
        "email":request.form['email'],
        "address":request.form['address'],
        "city":request.form['city'],
        "state":request.form['state'],
        "passwd":None
    }
    if request.form['passwd'] == request.form['confirm_passwd']:
        
    return redirect("/dashboard")