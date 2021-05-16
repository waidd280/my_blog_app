from flask import Blueprint, render_template
from .models import Question, User

questions = Blueprint('questions', __name__, url_prefix="/questions")

@questions.route('/<question_id>')
def test_q(question_id):
    page_question = Question.query.filter_by(id=question_id).first()
    question_author = User.query.filter_by(id=page_question.user_id).first().name

    return render_template('question_page.html', pagetitle=page_question.question_title, 
    page_question=page_question, question_author=question_author)
