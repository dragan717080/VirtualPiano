from flask import Flask
from config.config import *
from db_models import *
from flask_assets import Environment, Bundle

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    set_config(app.config, app.jinja_env)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()
    SESSION_TYPE = 'sqlalchemy'
    app.config.from_object(__name__)

    return app
