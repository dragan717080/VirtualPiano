from flask_sqlalchemy import SQLAlchemy

#configuration for the database
db = SQLAlchemy()

#configuration for app
def set_config(app_dict, env):

    BASE_DB = 'sqlite:///database/'
    tables = ['users', 'avatars', 'music_sheets', 'comments', 'messages']
    #setting app.config
    config_dict = {
        'SECRET_KEY': 'secretkey1',
        'SQLALCHEMY_DATABASE_URI': f'{BASE_DB}users.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_BINDS': {table: f'{BASE_DB}{table}.db' for table in tables},
        'TEMPLATES_AUTO_RELOAD': True,
        'CACHE_TYPE': 'redis',
        'CORS_HEADERS': 'Content-Type'
    }

    app_dict.update(config_dict)

    # setting jinja_env
    env.auto_reload = True
    env.cache = {}
