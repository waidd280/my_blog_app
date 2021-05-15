from flask import Blueprint
from .models import Question

questions = Blueprint('questions', __name__, url_prefix="/questions")

@questions.route('/<question_id>')
def test_q(question_id):
    page_question = Question.query.filter_by(id=question_id).first()
    return "Question Title: " + page_question.question_title
