from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user

site = Blueprint('site', __name__)

@site.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home.html', pagetitle="Home")
    
    return redirect(url_for('site.login'))

@site.route('/login')
def login():
    return render_template('login.html', pagetitle="Login")

@site.route('/login', methods=["POST"])
def login_post():
    email_entry = request.form.get('email_entry')
    password_entry = request.form.get('password_entry')

    print(email_entry)
    print(password_entry)

    return redirect(url_for('site.index'))