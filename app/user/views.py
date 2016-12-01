from flask import render_template, Blueprint, request, url_for, flash, redirect
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required, logout_user
from flask_mail import Message
from threading import Thread

from app.models import User
from .forms import RegisterForm, LoginForm
from app import db, mail, app

user_blueprint = Blueprint('user', __name__)

def flask_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text, error), 'info')

def send_async_email(msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, recipients, text_body, html_body):
	msg = Message(subject, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	thr = Thread(target=send_async_email, args=[msg])
	thr.start()	

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    	form = RegisterForm(request.form)
    	if request.method == 'POST':
        	if form.validate_on_submit():
            		try:
                		new_user = User(form.email.data, form.password.data)
                		new_user.authenticated = True
                		db.session.add(new_user)
                		db.session.commit()

				send_email('Registration', ['sydspitz@gmail.com'], 'Thanks for registering with Explore Your Shelf!', '<h3>Thanks for registering with Explore Your Shelf</h3>')		

                		flash('Thanks for registering!', 'success')
                		return redirect(url_for('book.index'))
            		except IntegrityError:
               			db.session.rollback()
                		flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
    	return render_template('register.html', form=form)




@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(email=form.email.data).first()
			if user is not None and user.is_correct_password(form.password.data):
				user.authenticated = True
                		db.session.add(user)
                		db.session.commit()
                		login_user(user)
                		flash('Thanks for logging in, {}'.format(current_user.email))
                		return redirect(url_for('book.index'))
			else:
				flash('ERROR! Incorrect login credentials.', 'error')
	return render_template('login.html', form=form)




@user_blueprint.route('/logout')
@login_required
def logout():
    	user = current_user
    	user.authenticated = False
    	db.session.add(user)
    	db.session.commit()
    	logout_user()
    	flash('Goodbye!', 'info')
    	return redirect(url_for('user.login'))


