from .. import app, db
from .form import *
from .model import Question
from app.register.view import *
from flask import render_template, request, flash, redirect, session, url_for

@app.route('/app.sli.do/event', methods=['GET', 'POST'])
def question():
    if request.args.get('event_id') != None :
        session['event_id'] = request.args.get('event_id')
    session['logged_in'] = False
    form = QuestionForm(request.form)
    db.create_all()
    questions = Question.query.filter_by(event_id=session['event_id']).all()
    if request.method == 'POST':
        question = Question(request.form['question'], session['event_id'], request.form['username'])
        db.session.add(question)
        db.session.commit()
        questions.append(question)
        flash('Question created successfully', 'success')
        return render_template('questions/create_question.html', form=QuestionForm(''), event=request.args.get('event_name'), questions=questions, number_of_question = len(questions))
    return render_template('questions/create_question.html', form=form, event=request.args.get('event_name'), questions=questions, number_of_question = len(questions))














