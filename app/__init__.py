from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .api.routes import api as api_blueprint
from .site.routes import site as site_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "\xfc\xad\x92\xecm$\xae\x95I\xb6\x0c1\x0fN \xba\xc3V\xbar7\x02j7"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////prod.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .api.routes import api as api_blueprint
    app.register_blueprint(api_blueprint)

    from .site.routes import site as site_blueprint
    app.register_blueprint(site_blueprint)

    return app
