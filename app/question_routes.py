from flask import Blueprint

questions = Blueprint('questions', __name__, url_prefix="/questions")

@questions.route('/practice-question')
def test_q():
    return "Test question page"
