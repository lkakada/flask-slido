from flask import Flask
from app.config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "LSDJFLSKDWO99374OKDFNCVKLDFLKLFDSLOID"
app.config.from_object(Configuration)

db = SQLAlchemy(app)

from app.views import *
from app.login.view import *
from app.register.view import *
from app.events.view import *
from app.questions.view import *