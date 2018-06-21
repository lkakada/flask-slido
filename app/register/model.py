from .. import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


def generate_uuid():
   return str(uuid.uuid4())[:6]

class User(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column('first_name', db.String(20))
    last_name = db.Column('last_name', db.String(20))
    username = db.Column('username', db.String(20), unique=True , index=True)
    email = db.Column('email',db.String(50),unique=True , index=True)
    password = db.Column('password' , db.String(10))
    registered_on = db.Column('registered_on' , db.DateTime)

    def __init__(self):
        self.user_id= generate_uuid()
        self.registered_on = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % (self.username)