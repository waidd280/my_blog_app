from flask import Flask

from .api.routes import api as api_blueprint
from .site.routes import site as site_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_blueprint)
    app.register_blueprint(site_blueprint)

    return app