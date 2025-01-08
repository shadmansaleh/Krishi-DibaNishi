from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, UserType  # Assuming you're using SQLAlchemy for the User model
from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to check if the user exists
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):  # Check hashed password
            session['logged_in'] = True
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            session['is_admin'] = user.usertype == UserType.admin
            flash('Login successful!', 'success')
            return redirect(url_for('pages.index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('pages/login.html')

@auth.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('user_id', None)
    session.pop('email', None)
    session.pop('is_admin', None)
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
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))

        # Hash the password before storing it
        if password is None or not password.strip():
            flash("Password cannot be empty.", "danger")
            return redirect(url_for('auth.register'))
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user instance and add it to the database
        new_user = User(username=username, email=email, password=hashed_password, usertype=UserType.user)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('pages/register.html')


@auth.route('/update_settings', methods=['GET', 'POST'])
def update_settings():
    if request.method == 'POST':
        # username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        user = User.query.filter_by(username=session['username']).first()

        # Update the user details
        # if username != user.username:
        #     user.username = username
        if email != user.email:
            user.email = email
        if password and password == confirm_password:
            user.password = generate_password_hash(password, method='pbkdf2:sha256')

        db.session.commit()
        # session['username'] = username  # Update session with new username

        flash('Settings updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('pages/settings.html')
