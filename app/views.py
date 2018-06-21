from flask import Flask, render_template, flash, request, session, url_for, redirect
from app import app
from app.form import *
# from app.events.view import *

@app.route('/', methods=['GET', 'POST'])
def index():
	# session['logged_in'] = False
	form = eventForm()
	# db.create_all()
	# event_id = form.event_code.data
	# if request.method == 'POST' and form.validate():
	# 	get_event = Event.query.filter_by(event_id=event_id.lower()).all()
	# 	if get_event:
	# 		session['event_id'] = event_id
	# 		return redirect(url_for('event_list_after_search', search=event_id))
	# 	else:
	# 		session['event_id'] = event_id
	# 		return redirect(url_for('event_list_after_error', search=event_id))
	return render_template('main/home.html', form=form)