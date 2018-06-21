from .. import app, db
from .form import *
from .model import User
from flask import Flask, render_template, flash, request, session, url_for, redirect

@app.route('/accounts.sli.do/signup', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	db.create_all()
	if request.method == 'POST' and form.validate():
		if User.query.filter_by(username=form.username.data).first():
			flash('Username already exists. Please enter different username.', 'danger')
			return redirect(url_for('register'))
		elif User.query.filter_by(email = form.email.data).first():
			flash('Email already exists. Please enter different email.', 'danger')
			return redirect(url_for('register'))
		else: 
			user = User()
			form.populate_obj(user)
			db.session.add(user)
			db.session.commit()
			session['logged_in'] = True
			session['username'] = user.username
			flash('User registered successfully.', 'success')
			return	redirect(url_for('index'))
	return render_template('user/register.html', form=form)