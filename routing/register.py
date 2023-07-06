from flask import render_template, request, redirect, Blueprint
from flask_login import login_user
from config.log_config import logging
from db_models import User
from helpers import Helpers

admins = Helpers.read_json_file('data/keys.json')

register_pages = Blueprint('register', __name__, url_prefix = '/')

@register_pages.route('/register', methods = ['POST'])
def register_post():
    email, username, password = request.form['email'], request.form['username'], request.form['password1']
    user = User(email=email, username=username, password=password)
    if user.username in admins:
        user.is_admin = True
    user_exists = User.get(email=user.email) and User.get(username=user.username)
    if not user_exists:
        User.save(user)
        login_user(user)

    return redirect('/')

@register_pages.route('/register')
def register():
    return render_template('register.html', all_users=User.get_all())
