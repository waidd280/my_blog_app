from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return render_template('home.html', pagetitle="Home")

@site.route('/login')
def login():
    return render_template('login.html', pagetitle="Login")