from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Question
from . import db

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return render_template('index.html', pagetitle="Home")

@site.route('/login')
def login():
    return render_template('login.html', pagetitle="Login")

@site.route('/login', methods=["POST"])
def login_post():
    email_entry = request.form.get('email_entry')
    password_entry = request.form.get('password_entry')

    user = User.query.filter_by(email=email_entry).first()
    if user is None:
        flash("No user associated with that email address")
        return render_template('login.html', pagetitle="Login")

    else:
        if not check_password_hash(user.password, password_entry):
            flash("Incorrect Password")
            return render_template('login.html', pagetitle="Login")

    login_user(user)
    return redirect(url_for('site.index'))

@site.route('/logout')
@login_required
def logout():
    logout_user()
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
    hashed_password = generate_password_hash(password, method="sha256")

    if not name == "" and not email == "" and not password == "":
        if User.query.filter_by(email=email).first() is None:
            new_user = User(email=email, password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('site.login'))

        flash("The email is already associated with an account")
        return render_template('signup.html', pagetitle="Sign Up")

    return redirect(url_for('site.signup'))

@site.route("/post-question")
@login_required
def add_question():
    return render_template("post_question.html", pagetitle="Post a Question")

@site.route("/post-question", methods=["POST"])
@login_required
def add_question_post():
    question_title = request.form.get('question-title')
    question_info = request.form.get('question-info')

    spaces_only = True
    if question_title == '':
        return redirect(url_for('site.index'))
    for char in question_title:
        if char != " ":
            spaces_only = False
            break
    if spaces_only:
        return redirect(url_for('site.index'))
    
    new_question = Question(question_title=question_title, 
    question_info=question_info, user_id=current_user.id)
    db.session.add(new_question)
    db.session.commit()
    
    return redirect(url_for('site.index'))

@site.route("/search")
def search_site():
    search_terms = request.args.get('terms')

    spaces_only = True
    if search_terms == '':
        return redirect(url_for('site.index'))
    for char in search_terms: 
        if char != ' ':
            spaces_only = False
            break
    
    if spaces_only: 
        return redirect(url_for('site.index'))
    """
    search_results = Question.query.filter_by(question_title=search_terms).all()
    print(search_results)"""
    search_results = Question.query.all()
    for search_result in search_results:
        search_result.user_id = User.query.filter_by(id=search_result.user_id).first().name

    return render_template('search_results.html', pagetitle="Search " + '"' + search_terms + '"', 
    results=search_results)
