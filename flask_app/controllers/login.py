from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users_model import users
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

@app.route("/login",methods=["POST"])
def login():
    category = "login"
    data = {
        "email":request.form["email"]
    }
    # if request.form["change_passwd"] == "change-passwd":
    #     session["email"] = request.form["email"]
    #     return redirect("/change_password")
    # else:
    if users.isValid(data,category) == False or len(request.form["passwd"]) == 0:
            flash("Invalid Email/Password empty")
            return redirect("/register_user")
    user_info = users.user_by_email(data)
    if not bcrypt.check_password_hash(user_info[0]["passwd"],request.form["passwd"]):
        flash("Invalid Email/Password")
        return redirect('/register_user')
    session["user"] = user_info[0]["first_name"]
    session["user_id"] = user_info[0]["id"]
    return redirect('/dashboard')

@app.route("/logout")
def logout():
    if session["user"] != None:
        session.clear()
        return redirect('/')
    
@app.route('/change_password')
def change_pass():
    return render_template("update_passwd.html", user_email =  session["email"])

@app.route('/update_password', methods =["POST"])
def update_passwd():
    category = "update-password"
    if request.form["passwd"] == request.form["confirm_passwd"]:
        
        data={
            "email":request.form["email"],
            "passwd": None #bcrypt.generate_password_hash(request.form["passwd"])
        }
        
        info = users.user_by_email(data)
        print(info)
        users.isValid(data,category)
        if request.form["passwd"] != request.form["confirm_passwd"]:
            flash("Invalid Email/Password")
            return redirect('/')
        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,}',request.form["passwd"]):
            flash("Invalid PASSWORD requirement {{PASSWORD_REGEX}}")
            return redirect('/register_user')
        else: 
            data["passwd"] = bcrypt.generate_password_hash(request.form["passwd"])
            users.update_passwd(data)
            userinf = users.get_info(data)
            session["user"] = userinf[0]["first_name"]
            session["user_id"] = userinf[0]["id"]
            return redirect('/dashboard')
        
    return redirect("/change_password")