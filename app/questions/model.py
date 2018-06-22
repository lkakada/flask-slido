from .. import db
from datetime import datetime

class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column('event_id', db.String(20))
    question = db.Column('question', db.String(500))
    username = db.Column('username', db.String(50), default='anonymous')
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self, question, event_id, username=''):
        self.question = question
        self.event_id = event_id
        self.registered_on = datetime.now()
        if username != '':
        	self.username = username