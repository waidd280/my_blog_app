from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import Question, User

questions = Blueprint('questions', __name__, url_prefix="/questions")

@questions.route('/<question_id>')
def question_page(question_id):
    page_question = Question.query.filter_by(id=question_id).first()
    question_author = User.query.filter_by(id=page_question.user_id).first().name

    print(page_question.answers)

    return render_template('question_page.html', pagetitle=page_question.question_title, 
    page_question=page_question, question_author=question_author)

@questions.route('/<question_id>', methods=["POST"])
def question_page_post(question_id):
    if current_user.is_authenticated:
        print("authenticated")
    return redirect('/questions/' + question_id)
