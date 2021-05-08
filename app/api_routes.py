from flask import Blueprint
from flask_login import login_required
from . import db
from .models import User, Question

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/allquestions')
@login_required
def show_all_questions():
    questions_dict = dict()
    questions = Question.query.all()
    
    for question in questions:
        question_author = User.query.filter_by(id=question.user_id).first().name

        questions_dict.update({question.id: {'question-title': question.question_title,
        'question-info': question.question_info, 'question-author': question_author}})
    
    return questions_dict
