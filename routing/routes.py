from flask import render_template, Blueprint, request
from flask_login import current_user
from flask_cors import cross_origin
from helpers import Helpers
from db_models import MusicSheet, User, Comment, Quote
import numpy as np

index_pages = Blueprint('index', __name__, url_prefix='/')

@index_pages.route('/')
@cross_origin()
def index():
    data = Helpers.read_json_file('keys')
    keys, keyboard_notes, keyboard_sounds = data['keys'], data['notes'], data['sounds']
    loaded_music_sheet = request.args.get('loaded-sheet')
    if loaded_music_sheet != None:
        loaded_sheet = MusicSheet.get(title = loaded_music_sheet)
    else: loaded_sheet = None
    params = {
        'keyboard_notes': keyboard_notes,
        'keyboard_sounds': keyboard_sounds,
        'keys': keys,
        'most_active_users': Helpers.get_most_active_users(),
        'latest_users': User.get_latest(),
        'loaded_sheet': loaded_sheet,
        'random_quote': np.random.choice(Quote.get_all())
    }
    if current_user.is_anonymous:
        return render_template('index.html', **params)
    
    user_params = {
        'loggedinuser': current_user.username,
        'avatar': current_user.avatar.image if current_user.avatar is not None else None,
        'avatar_format': current_user.avatar.image_format if current_user.avatar is not None else None
    }
    params.update(user_params)
    return render_template('index.html', **params)
