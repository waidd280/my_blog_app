from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user
from werkzeug.security import generate_password_hash
from .models import User
from . import db

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

@site.route('/signup')
def signup():
    return render_template('signup.html', pagetitle="Sign Up")

@site.route('/signup', methods=["POST"])
def signup_post():
    form = request.form

    name = form.get("name_entry")
    email = form.get("email_entry")
    password = form.get("password_entry")
    hashed_password = generate_password_hash(password)

    if not name == "" and not email == "" and not password == "":
        if User.query.filter_by(email=email).first() is None:
            new_user = User(email=email, password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('site.login'))
            
        flash("The email is already associated with an account")
        return redirect(url_for('site.signup'))

    flash("All fields must be filled")
    return redirect(url_for('site.signup'))
