from flask import flash
from flask_app import app
from flask_app.config.myConnection import connect_to_mysql
from flask_bcrypt import Bcrypt
import re
bcrypt =  Bcrypt(app)
PASSWORD_REGEX = re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}')
phone_regex = re.compile(r'[0-9]{10,}')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class users:
    db = "bible_app_schema"
    def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name =data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.passwd = data['passwd']
    
# get information of all users from database
    @classmethod
    def get_users(cls):
        query = """select * from users"""
        data = connect_to_mysql(cls.db).query_db(query)
        return data

    @classmethod
    def add_user(cls,data):
        query = """INSERT INTO users (first_name, last_name,
        email,
        phone,
        address,
        city,
        state,
        passwd,created_at) VALUES(%(first_name)s, %(last_name)s,%(email)s,%(phone)s,%(address)s,%(city)s,
        %(state)s,
        %(passwd)s,NOW())"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        print(info)
    
    
    @classmethod
    def update_user(cls,data):
        query = """UPDATE users SET first_name =%(first_name)s, last_name=%(last_name)s,email=%(email)s,phone=%(phone)s,address = %(address)s,city=%(city)s,
        state=%(state)s,
        passwd = %(passwd)s,update_at = NOW() WHERE id = %(id)s;"""
        connect_to_mysql(cls.db).query_db(query,data)
        
    @classmethod
    def user_by_email(cls,data):
        query = """select * from users where email = %(email)s"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        return info
    
        
    @staticmethod
    def isValid(data,category):
        valid =True
        if len(data) > 2:
            if len(data["first_name"]) <3:
                flash("first name need length greater than 2",category)
                valid=False
            if len(data["last_name"]) <3:
                flash("Last name length must be greater than 2",category)
                valid=False
            if not EMAIL_REGEX.match(data["email"]):
                flash("Invalid email address",category)
                valid=False
        else:
            if data["email"] == 0:
                valid = False
                flash("email/password are empty",category)
        return valid