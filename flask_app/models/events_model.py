from flask import flash
from flask_app.config.myConnection import connect_to_mysql

class bible_event:
    db = "bible_app_schema"
    def __init__(self,data):
            self.title_verses= data['title']
            self.location = data['location']
            self.event_date = data['event_date']
            self.time = data['time']
            self.details = data['details'],
            self.user_id = data['user_id']
            self.created_at = data['created_at']
    
# get information of all users from database
    @classmethod
    def get_events(cls):
        query = """select * from event1"""
        data = connect_to_mysql(cls.db).query_db(query)
        return data
    
    @classmethod
    def event_by_id(cls,data):
        query = """select * from event1 where id=%(id)s;"""
        info = connect_to_mysql(cls.db).query_db(query,data)
        return info

    @classmethod
    def add_event(cls,data):
        query = """INSERT INTO event1 (title,location,event_date,time,details,user_id,created_at) VALUES(%(title)s, %(location)s,%(event_date)s,%(time)s,%(details)s,%(user_id)s,NOW());"""
        connect_to_mysql(cls.db).query_db(query,data)
    
    
    @classmethod
    def update_events(cls,data):
        query = """UPDATE event1 SET title = %(title)s, location = %(location)s, event_date%(event_date)s,time= %(time)s,details = %(details)s,user_id = %(user_id)s,updated_at=NOW() WHERE id = %(id)s;"""
        connect_to_mysql(cls.db).query_db(query,data)
        
        
    @classmethod
    def past_events(cls):
        query = """select * from event1 where event_date < CURRENT_DATE()"""
        info = connect_to_mysql(cls.db).query_db(query)
        return info
    
    @classmethod
    def  remove_event(cls,data):
        query = """delete from event1 where id=%(id)s;"""
        connect_to_mysql(cls.db).query_db(query,data)
        
    @classmethod
    def get_event_users(cls):
        query = """select event1.id,event1.title,event1.location,event1.event_date,event1.time,event1.details,users.first_name,users.last_name from event1 join users on event1.user_id = users.id;"""
        info = connect_to_mysql(cls.db).query_db(query)
        print(info)
        return info