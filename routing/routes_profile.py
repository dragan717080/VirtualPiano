from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from db_models import User, Avatar
from helpers import read_json_file
import os

profile_pages = Blueprint('profile', __name__, url_prefix = '/')

@profile_pages.route('/profile', methods=['POST'])
def profile_post():
    upload_path = read_json_file('data/keys.json')['upload_path']
    #user has no avatar yet
    if request.form['submit'] == 'GET_AVATAR': 
        profile_picture = request.files['profile_picture']
        img_path = os.path.join(os.getcwd(), upload_path, profile_picture.filename)
        profile_picture.save(img_path)
        current_user.avatar.img_link = profile_picture.filename
        current_user.save()
        return redirect(request.url)
    #user has avatar
    else:
        profile_picture = request.files['profile_picture']
        if profile_picture.filename != '':
            profile_picture.save(os.path.join(upload_path, profile_picture.filename))
            current_user.avatar.img_link = profile_picture.filename
            current_user.save()
        else:
            return redirect(request.url)
        return redirect(request.url)

@profile_pages.route('/profile')
def profile():
    params = {
        'loggedinuser': current_user.username,
        'profilecreated': current_user.created_at.strftime('%Y %m %d'),
        'user_has_avatar': False,
        'is_admin': current_user.is_admin,
        'music_sheets': current_user.music_sheets,
        'inbox_messages': [],
        'avatar': current_user.avatar.img_link
    }
    print(current_user.avatar.img_link)
    return render_template('profile.html', **params)
