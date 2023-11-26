#!/usr/bin/python3


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'you_and_i_key_secret'
db = SQLAlchemy(app)


from models import User, Room, ChatMessage

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = 'your_secret_key'

app.config.from_object(Config)

def validate_password(password, confirm_password):
    # Check if password and confirm password match
    if password != confirm_password:
        flash('password_mismatch', 'error')
        return False

    # Check if password meets your requirements
    if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        flash('password_requirements', 'error')
        return False

    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        # For simplicity, just checking if the fields are not empty
        if username and password:
            # Successful login, redirect to the home page
            return redirect(url_for('index'))
        else:
            # Login failed, you might want to show an error message
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    message = None
    if request.method == 'POST':
        # Logic to handle the password reset request
        email = request.form.get('email')
        # Generate a unique token, send an email with the token, etc. (implementation not provided here)

        # For simplicity, you can redirect to a success page
        message = "If your email address exists in our database, you will receive a password recovery link at your email address in a few minutes."

    return render_template('password_reset_request.html', message=message)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if password and confirm password match
        if not validate_password(password, confirm_password):
            return redirect(url_for('signup', email=email, username=username))

        # Redirect to login page after signup
        return redirect(url_for('login'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
