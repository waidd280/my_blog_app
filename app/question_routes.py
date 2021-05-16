from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user
from .models import Question, User, Answer
from . import db

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
        answer_content = request.form.get("answer-content")
        
        if len(answer_content) > 10:
            new_answer = Answer(answer_text=answer_content, user_id=current_user.id, 
            question_id=int(question_id))
            db.session.add(new_answer)
            db.session.commit()

    return redirect('/questions/' + question_id)
