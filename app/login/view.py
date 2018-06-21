from .. import app, db
from .form import *
from app.register.view import *
from flask import render_template, request, flash, redirect, url_for, session


@app.route('/accounts.sli.do/login', methods=['GET', 'POST'])
def login():
    form = Login()
    session['logged_in'] = False
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                session['logged_in'] = True
                session['user_id'] = user.user_id
                session['username'] = user.username
                flash('You logged in successfully.', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid password. Please try again!', 'danger')
        else: 
            flash('Username does not exist. Please try again!', 'danger')
    return render_template('user/login.html', form=form)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
