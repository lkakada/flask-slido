from .. import app, db
from .form import *
from .model import Event
from datetime import datetime
import time
from flask import render_template, request, flash, redirect, session, url_for, jsonify
from app.form import *
from app.questions.view import *
from app.questions.form import QuestionForm


def date_format(time_str):
	return time_str.strftime("%d %b, %H:%M %p")

def checking_event(model_name, filter):
	past = datetime.now()
	now = past.strftime("%d.%m.%Y")
	now1 = time.strptime(now, "%d.%m.%Y")
	past_event = []
	active_event = []
	result = model_name.query.filter_by(user_id=filter).all()
	for i in result:
		if time.strptime(i.date_to, "%d.%m.%Y") >= now1:
			active_event.append(i)
		else:
			past_event.append(i)
	return [past_event, active_event]

def checking_event_status(model_name):
	past = datetime.now()
	now = past.strftime("%d.%m.%Y")
	now1 = time.strptime(now, "%d.%m.%Y")
	get_event_status = ""
	for i in model_name: 
		if time.strptime(i.date_to, "%d.%m.%Y") >= now1:
			get_event_status = "Your event is still active."
		else:
			get_event_status = "Your event has finished."
	return get_event_status


@app.route('/admin.sli.do/event', methods=["GET", "POST"])
def event_dashboard():
	form = CreateForm()
	questionform = QuestionForm()
	searchform = SearchForm()
	session['logged_in'] = True
	username = session['username']
	email = session['email']
	first_name = session['first_name']
	last_name = session['last_name']
	
	if request.method == 'POST' and form.validate():
		event = Event(session['user_id'], form.event_name.data, form.date_from.data, form.date_to.data)
		db.session.add(event)
		db.session.commit()
		flash('Event created successfully.', 'success')
		return redirect(url_for('event_dashboard'))
		
	past_event = checking_event(Event, session['user_id'])[0]
	active_event = checking_event(Event, session['user_id'])[1]

	return render_template('events/event_dashboard.html', questionform = questionform, form=form, searchform=searchform, username=username, email=email, first_name=first_name, last_name=last_name, active_event=active_event, past_event=past_event)

@app.route('/admin.sli.do/event/<string:event_id>/dashboard', methods=['GET'])
def admin_event_dashboard(event_id):
	questionform = QuestionForm()
	get_event_id = event_id
	session['logged_in'] = True
	username = session['username']
	email = session['email']
	first_name = session['first_name']
	last_name = session['last_name']
	session['event_id'] = event_id
	get_event_name = Event.query.filter_by(event_id=event_id).first()
	get_events = Event.query.filter_by(event_id=event_id).all()
	get_questions_by_event_id = Question.query.filter_by(event_id=get_event_id).all()

	get_event_status = checking_event_status(get_events)
	get_date_to = datetime.strptime(get_event_name.date_to, "%d.%m.%Y")
	get_date_from = datetime.strptime(get_event_name.date_from, "%d.%m.%Y")

	return render_template('events/admin_event_dashboard.html', questionform = questionform, get_date_to = get_date_to, get_date_from=get_date_from, get_event_id=get_event_id, get_event_name=get_event_name.event_name, questions=get_questions_by_event_id, get_event_status=get_event_status, username=username, email=email, first_name=first_name, last_name=last_name, form=CreateForm(), event_id = session['event_id'])

@app.route('/admin.sli.do/event/update/<string:event_id>', methods=['GET', 'POST'])
def event_update(event_id):
    form = CreateForm(request.form)
    session['event_id'] = event_id
    if request.method == 'POST' and form.validate():
        updated_data = {
            'event_name': request.form['event_name'],
            'date_from': request.form['date_from'],
            'date_to': request.form['date_to']
        }
        db.session.query(Event).filter_by(event_id=event_id).update(updated_data)
        db.session.commit()
        flash('Event updated successfully.', 'success')
        return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))
    return redirect(url_for('event_dashboard'))

@app.route('/app.sli.do/', methods=['GET', 'POST'])
def event_list_after_search():
    form = eventForm()
    event_id = form.event_code.data
    if request.method == 'POST' and form.validate():
        get_event = Event.query.filter_by(event_id=event_id.lower()).all()
        if get_event:
            session['event_id'] = event_id
            return redirect(url_for('event_list_after_search', search=event_id))
        else:
            session['event_id'] = event_id
            return redirect(url_for('event_list_after_error', search=event_id))
    events = Event.query.filter_by(event_id=session['event_id'].lower()).all()
    return render_template('navbar/question_navbar_search.html', events=events, form=form)

@app.route('/app.sli.do.disactive/', methods=['GET', 'POST'])
def event_list_after_error():
	form = eventForm()
	event_id = form.event_code.data
	if request.method == 'POST' and form.validate():
		get_event = Event.query.filter_by(event_id=event_id.lower()).all()
		if get_event:
			session['event_id'] = event_id
			return redirect(url_for('event_list_after_search', search=event_id))
		else:
			session['event_id'] = event_id
			return redirect(url_for('event_list_after_error', search=event_id))
	return render_template('events/error_event.html', form=form)

@app.route('/event/delete/<string:event_id>')
def event_delete(event_id):
    db.session.query(Event).filter_by(event_id=event_id).delete()
    db.session.commit()
    flash('Event deleted successfully.', 'success')
    return redirect(url_for('event_dashboard'))


@app.route('/admin.sli.do/events', methods=['GET'])
def getEvent():
	rec_list = []
	get_event = Event.query.filter_by(event_id=session['event_id']).all()
	for record in get_event:
		rec_dict = {'event_id': record.event_id, 'user_id': record.user_id, 'event_name': record.event_name, 'date_from': record.date_from, 'date_to': record.date_to, 'registered_on': record.registered_on}
		rec_list.append(rec_dict)
	return jsonify(rec_list)





