from .. import db
from datetime import datetime
import uuid


def generate_uuid():
   return str(uuid.uuid4())[:6]

class Event(db.Model):

    event_id = db.Column(db.String, primary_key = True)
    user_id = db.Column('user_id', db.String(20))
    event_name = db.Column('event_name', db.String(30))
    date_from = db.Column('date_from', db.String(20))
    date_to = db.Column('date_to', db.String(20))
    registered_on = db.Column('registered_on' , db.DateTime)


    def __init__(self , user_id, event_name, date_from, date_to):
        self.user_id = user_id
        self.event_name = event_name
        self.date_from = date_from
        self.date_to = date_to
        self.registered_on = datetime.utcnow()
        self.event_id = generate_uuid()
