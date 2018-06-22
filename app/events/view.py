from .. import app, db
from .form import *
from .model import Event
from datetime import datetime
from flask import render_template, request, flash, redirect, session, url_for, jsonify
from app.form import *
# from app.questions.view import *


def date_format(time_str):
	return time_str.strftime("%d %b, %H:%M %p")

def checking_event_status(model_name, filter):
	past = datetime.now()
	now = past.strftime("%d.%m.%Y")
	past_event = []
	active_event = []
	result = model_name.query.filter_by(user_id=filter).all()
	for i in result:
		if i.date_to >= now:
			active_event.append(i)
		else:
			past_event.append(i)
	return [past_event, active_event]


@app.route('/admin.sli.do/event', methods=["GET", "POST"])
def event_dashboard():
	form = CreateForm()
	searchform = SearchForm()
	session['logged_in'] = True
	username = session['username']
	
	if request.method == 'POST' and form.validate():
		event = Event(session['user_id'], form.event_name.data, form.date_from.data, form.date_to.data)
		db.session.add(event)
		db.session.commit()
		flash('Event created successfully.', 'success')
		return redirect(url_for('event_dashboard'))
		
	past_event = checking_event_status(Event, session['user_id'])[0]
	active_event = checking_event_status(Event, session['user_id'])[1]

	return render_template('events/event_dashboard.html', form=form, searchform=searchform, username=username, active_event=active_event, past_event=past_event)



















