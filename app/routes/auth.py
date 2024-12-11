from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User  # Assuming you're using SQLAlchemy for the User model
# from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # handle login logic here
        username = request.form['username']
        password = request.form['password']
        if username == 'user' and password == 'pass':
            session['logged_in'] = True 
            flash('Login successful!', 'success')
            return redirect(url_for('pages.index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('pages/login.html')

@auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('pages.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if password and confirm password match
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth.register'))

        # Check if user already exists
        # user = User.query.filter_by(username=username).first()
        # if user:
        #     flash('Username already exists. Please choose a different one.', 'danger')
        #     return redirect(url_for('auth.register'))
        # 
        # user = User.query.filter_by(email=email).first()
        # if user:
        #     flash('Email already registered. Please choose a different one.', 'danger')
        #     return redirect(url_for('auth.register'))

        # Hash the password before storing it
        # hashed_password = generate_password_hash(password, method='sha256')
        #
        # Create a new user instance and add it to the database
        # new_user = User(username=username, email=email, password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('pages/register.html')
