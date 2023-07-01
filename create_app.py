from flask import Flask
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from config.config import *
from db_models import *
from base64 import b64encode

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    set_config(app.config, app.jinja_env)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()
    SESSION_TYPE = 'sqlalchemy'
    app.config.from_object(__name__)

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    #for blobs
    @app.template_filter('b64encode')
    def base64_encode(value):
        return b64encode(value).decode('utf-8')

    return app
