from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import InputRequired


class QuestionForm(Form):
	question = TextAreaField(validators=[InputRequired('Please enter question')])
	username = StringField()