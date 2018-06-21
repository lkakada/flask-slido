from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import InputRequired

class eventForm(Form):
	event_code = StringField(validators=[InputRequired('Please enter event code')])