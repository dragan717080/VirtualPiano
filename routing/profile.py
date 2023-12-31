from flask import  render_template, request, redirect, Blueprint
from flask_login import login_required, current_user
from db_models import User, Avatar, Message
from helpers import Helpers

profile_pages = Blueprint('profile', __name__, url_prefix = '/')

@profile_pages.route('/profile', methods=['POST'])
def profile_post():
    profile_picture = request.files['profile_picture']
    img_format = profile_picture.filename.split('.')[-1]
    filename = profile_picture.filename

    # User has no avatar
    if request.form['submit'] == 'GET_AVATAR':
        profile_picture.seek(0)
        avatar = Avatar(image = profile_picture.read(), image_format = img_format, user_id = current_user.id)
        avatar.save()

        current_user.avatar = avatar
        current_user.save()
        return redirect(request.url)
    # User has avatar
    else:
        if filename != '':
            avatar = current_user.avatar
            profile_picture.seek(0)
            avatar.image = profile_picture.read()
            avatar.image_format = img_format
            avatar.save()
        return redirect(request.url)

@profile_pages.route('/profile')
def profile():
    params = {
        'loggedinuser': current_user.username,
        'profilecreated': current_user.created_at.strftime('%Y %m %d'),
        'user_has_avatar': False,
        'is_admin': current_user.is_admin,
        'music_sheets': current_user.music_sheets,
        'inbox_messages': Message.query.filter_by(recipient_id = current_user.id).all(),
        'avatar': current_user.avatar.image if current_user.avatar is not None else None,
        'avatar_format': current_user.avatar.image_format if current_user.avatar is not None else None
    }
    return render_template('profile.html', **params)

@profile_pages.route('/inbox', methods = ['GET', 'POST'])
@login_required
def inbox():
    params = {
        'loggedinuser': current_user.username,
        'inbox_messages': Helpers.get_inbox_messages(current_user.id),
        'avatar': current_user.avatar.image if current_user.avatar else None,
        'avatar_format': current_user.avatar.image_format if current_user.avatar else None,
        'all_emails': []
    }
    # Need to pass list of dicts containing usernames and avatars
    return render_template('inbox.html', **params)
