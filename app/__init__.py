from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    from .secret_key import set_key, get_key

    set_key()
    app.config["SECRET_KEY"] = get_key()
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .api_routes import api as api_blueprint
    app.register_blueprint(api_blueprint)

    from .site_routes import site as site_blueprint
    app.register_blueprint(site_blueprint)

    from .question_routes import questions as questions_blueprint
    app.register_blueprint(questions_blueprint)

    return app
