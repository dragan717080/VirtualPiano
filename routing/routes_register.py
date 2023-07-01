from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from config.log_config import logging
from db_models import db, User
from helpers import read_json_file

admins = read_json_file('data/keys.json')

register_pages = Blueprint('register', __name__, url_prefix = '/')

@register_pages.route('/register', methods = ['POST'])
def register_post():
    email, username, password = request.form['email'], request.form['username'], request.form['password1']
    logging.debug(email, username, password)
    nu = User(email=email, username=username, password=password)
    if nu.username in admins:
        nu.isadmin = True
    user_exists = len(db.session.query(User).filter_by(email=nu.email).all()) > 0 and len(
        db.session.query(User).filter_by(username=nu.username).all()) > 0
    logging.debug(user_exists)
    if not user_exists:
        User.save(nu)
        login_user(nu)

    return redirect('/')

@register_pages.route('/register')
def register():
    logging.debug(User.find_all(User))
    return render_template('register.html', all_users=User.find_all(User))
