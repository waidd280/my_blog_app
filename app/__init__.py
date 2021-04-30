from flask import Flask

from .api.routes import api as api_blueprint
from .site.routes import site as site_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_blueprint)
    app.register_blueprint(site_blueprint)

    app.secret_key = "\xfc\xad\x92\xecm$\xae\x95I\xb6\x0c1\x0fN \xba\xc3V\xbar7\x02j7"

    return app