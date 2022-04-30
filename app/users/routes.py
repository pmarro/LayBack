from flask import Blueprint, redirect, render_template, request, url_for
from app.users.models import User
from app.design_guides.models import Designguide #DesignguideElement
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app.extensions.database import db

blueprint = Blueprint('users', __name__)


@blueprint.route('/register')
def register():
      return render_template('users/register.html')
 
@blueprint.post('/register')
def post_register():
    try:
        password_input = request.form.get('password')
        email_input = request.form.get('email')
        if User.query.filter_by(company_email = email_input).first():
            raise Exception('This email address is already beeing used.')
        elif len(password_input) < 10:
            raise Exception ('Your password should be more than 10 characters long.') 
            
        user = User(
            company_email = request.form.get('email'),
            password = generate_password_hash(password_input),
            name = request.form.get('name')
        )
        
        user.save()

        designguide = Designguide(
            user = user
        )

        designguide.save()

        login_user(user)
        return render_template('design_elements/welcome.html')
    except Exception as error_message:
        error = error_message or 'An error occurred while creating a user. Please make sure to enter valid data.'
        
        return render_template('users/register.html', error=error)


@blueprint.get('/login')
def get_login():
  return render_template('users/login.html')

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(company_email = request.form.get('email')).first() 
        if not user:
            raise Exception ('This email address has not been registered yet')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception ('The password does not appear to be correct')
        login_user(user)
        return render_template('design_elements/welcome.html')

    except Exception as error_message:
        error = error_message or 'An error occurred while logging in. Please verify your email and password.'
        return render_template('users/login.html', error=error)

@blueprint.get('/logout')
def logout():
    logout_user()

    return redirect(url_for('simple_pages.index'))