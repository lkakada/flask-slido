from .. import app, db
from .form import *
from .model import Question
from app.register.view import *
from flask import render_template, request, flash, redirect, session, url_for, jsonify

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
        flash('Question has been sent successfully', 'success')
        return render_template('questions/create_question.html', form=QuestionForm(''), event=request.args.get('event_name'), questions=questions, number_of_question = len(questions))
    return render_template('questions/create_question.html', form=form, event=request.args.get('event_name'), questions=questions, number_of_question = len(questions))


@app.route('/app.sli.do/question/<string:id>')
def question_delete(id):
    session['question_id'] = id
    question = Question.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Question deleted successfully.', 'success')
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))

@app.route('/admin.sli.do/question/<int:id>', methods=['GET'])
def getQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == id:
            rec_dict = {'id': record.id, 'event_id': record.event_id, 'question': record.question, 'username': record.username, 'registered_on': record.registered_on}
            rec_list.append(rec_dict)
    return jsonify(rec_list)

@app.route('/admin.sli.do/question/update/<string:event_id>', methods=['GET', 'POST'])
def question_update(event_id):
    form = QuestionForm(request.form)
    session['event_id'] = event_id
    if request.method == 'POST' and form.validate():
        updated_data = {
            'question': request.form['question'],
        }
        get_questions = Question.query.filter_by(event_id=event_id).all()
        for question in get_questions:
            if question.id == session['question_id']:
                db.session.query(Question).filter_by(id=session['question_id']).update(updated_data)
                db.session.commit()
                flash('Question updated successfully.', 'success')
                return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))
    return redirect(url_for('admin_event_dashboard'))

@app.route('/admin.sli.do/question/starred/<int:id>', methods=['GET'])
def getStarredQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.starred = True
            starred_question.starred_color = "#FFA500"
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))


@app.route('/admin.sli.do/question/unstarred/<int:id>', methods=['GET'])
def getUnStarredQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.starred = False
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))

@app.route('/admin.sli.do/question/completed/<int:id>', methods=['GET'])
def getCompletedQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.completed = True
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))


@app.route('/admin.sli.do/question/incompleted/<int:id>', methods=['GET'])
def getIncompletedQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.completed = False
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))


@app.route('/admin.sli.do/question/isHighlighted/<int:id>', methods=['GET'])
def getIsHighlightedQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.isHighlighted = True
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))

@app.route('/admin.sli.do/question/unHighlighted/<int:id>', methods=['GET'])
def getUnHighlightedQuestion(id):
    rec_list = []
    session['question_id'] = id
    get_question = Question.query.filter_by(event_id=session['event_id']).all()
    for record in get_question:
        if record.id == session['question_id']:
            starred_question = Question.query.filter_by(id = session['question_id']).first()
            starred_question.isHighlighted = False
            db.session.commit()
    return redirect(url_for('admin_event_dashboard', event_id=session['event_id']))

    












