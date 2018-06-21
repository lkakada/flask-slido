from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import InputRequired, Email, Length

class RegistrationForm(Form):
	last_name = StringField(validators=[InputRequired('Please enter your last name.')])
	first_name = StringField(validators=[InputRequired('Please enter your first name.')])
	username = StringField(validators=[InputRequired('Please enter your first name.')])
	email = TextField(validators=[InputRequired('Please enter your email address.')])
	password = PasswordField(validators=[InputRequired('Please enter a password.')])