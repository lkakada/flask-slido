from .. import db
from datetime import datetime

class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id        = db.Column('event_id', db.String(20))
    question        = db.Column('question', db.String(500))
    username        = db.Column('username', db.String(50), default='anonymous')
    starred         = db.Column('starred', db.Boolean, default=False)
    completed       = db.Column('completed', db.Boolean, default=False)
    isHighlighted   = db.Column('isHighlighted', db.Boolean, default=False)
    like            = db.Column('like', db.Boolean, default = False)
    moderate        = db.Column('moderate', db.Boolean, default = False)
    registered_on   = db.Column('registered_on' , db.DateTime)



    def __init__(self, question, event_id, username=''):
        self.question       = question
        self.event_id       = event_id
        self.registered_on  = datetime.now()
        self.starred        = False
        self.completed      = False
        self.isHighlighted  = False
        self.like           = False
        self.moderate       = False
        if username != '':
        	self.username   = username