from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import InputRequired

class Login(Form):
	username = StringField(validators=[InputRequired('Please enter your first name.')])
	password = PasswordField(validators=[InputRequired('Please enter a password.')])