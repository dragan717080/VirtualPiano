from flask import render_template, Blueprint, request
from flask_login import current_user
from flask_cors import cross_origin
from helpers import read_json_file
from db_models import MusicSheet, User
import base64

index_pages = Blueprint('index', __name__, url_prefix='/')

@index_pages.route('/')
@cross_origin()
def index():
    latest_users = User.query.order_by(User.created_at).all()
    latest_users.reverse()
    data = read_json_file('data/keys.json')
    keys, keyboard_notes, keyboard_sounds = data['keys'], data['notes'], data['sounds']
    loaded_music_sheet = request.args.get('loaded_sheet')
    if loaded_music_sheet != None:
        loaded_sheet = MusicSheet.query.filter_by(title = loaded_music_sheet + ".txt").first()
    else: loaded_sheet = None
    params = {
        'keyboard_notes': keyboard_notes,
        'keyboard_sounds': keyboard_sounds,
        'keys': keys,
        'most_active_users': [],
        'latest_users': latest_users
    }
    if current_user.is_anonymous:
        return render_template('index.html', **params)
    user_params = {
        'loggedinuser': current_user.username,

        'latest_users': latest_users
    }
    params.update(user_params)
    print(current_user.avatar.image)
    print(current_user.avatar.image_format)
    return render_template('index.html', **params)
