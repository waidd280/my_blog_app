from flask import Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return "Welcome to the home page"