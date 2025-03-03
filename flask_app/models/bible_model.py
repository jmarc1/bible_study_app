from flask import flash
from flask_app.config.myConnection import connect_to_mysql

class bible:
    db = "bible_app_schema"
    def __init__(self,data):
            self.title_verses= data['title_verses']
            self.chapter_verse = data['chapter_verses']
            self.date_add = data['date_add']
            self.verse = data['verse']
    
# get information of all users from database
    @classmethod
    def get_users(cls):
        query = """select * from verses"""
        data = connect_to_mysql(cls.db).query_db(query)
    
        return data

    @classmethod
    def add_verse(cls,data):
        query = """INSERT INTO verse (title_verses,chapter_verse,date_add,verse) VALUES(%(title_verses)s, %(chapter_verse)s,NOW(),%(verse)s)"""
        connect_to_mysql(cls.db).query_db(query,data)
    
    
    @classmethod
    def update_verse(cls,data):
        query = """UPDATE users SET title_verses =%(title_verses)s, chaper_verse=%(chapter_verse)s,date_add=NOW(),verse = %(verse)s WHERE id = %(id)s;"""
        connect_to_mysql(cls.db).query_db(query,data)