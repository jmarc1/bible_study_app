from flask_app import app
from flask_app.models.users_model import users
from flask import flash,render_template,redirect,session,request
from flask_bcrypt import Bcrypt
import re
bcrypt =  Bcrypt(app)
PASSWORD_REGEX = re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}')
phone_regex = re.compile(r'[0-9]{10,}')

@app.route('/new_user', methods =["POST"])
def add_user():
    category = 'register'
    if request.form['action'] == 'cancel':
        return redirect('/')
    elif request.form['action'] == 'login':
        return redirect('/login')
    data={
        "first_name":request.form['first_name'],
        "last_name":request.form["last_name"],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "address":request.form['address'],
        "city":request.form['city'],
        "state":request.form['state'],
        "passwd":None
    }
    #print(PASSWORD_REGEX)
    if users.isValid(data,category) != True:
        return redirect('/register_user')
    if request.form["passwd"] != request.form["confirm_passwd"]:
        flash("Invalid Email/Password")
        return redirect('/')
    elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,}',request.form["passwd"]):
        flash("Invalid PASSWORD requirement {{PASSWORD_REGEX}}")
        return redirect('/register_user')
    else:
        data["passwd"] = bcrypt.generate_password_hash(request.form["passwd"])
        users.add_user(data)
        userinf = users.user_by_email(data)
        session["user"] = data["first_name"]
        session["user_id"] = userinf[0]["id"]
        return redirect('/dashboard')
