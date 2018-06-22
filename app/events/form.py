from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextField, DateField
from wtforms.validators import InputRequired

class CreateForm(Form):
	event_name = StringField(validators=[InputRequired('Please enter event name')])
	date_from = StringField(validators=[InputRequired('Please select date from')])
	date_to = StringField(validators=[InputRequired('Please select date to')])

class SearchForm(Form):
	search = StringField(validators=[InputRequired('Search')])