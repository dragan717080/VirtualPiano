from flask import render_template, request, redirect, Blueprint
from flask_login import login_user, current_user
from config.log_config import logging
from db_models import User

login_pages = Blueprint('login', __name__,
    template_folder='Templates/', static_folder='static', url_prefix = '/')

@login_pages.route('/login/', methods = ['POST'])
def login_post():
    username = request.form['username_1']
    password = request.form['password_1']
    check_login = User.find(username=username)
    if (check_login == None):
        if (current_user.is_anonymous):
            return render_template('login.html', handle=1)
    passwords_match = check_login.password == password
    if (check_login):
        if not passwords_match:
            return render_template('login.html', handle=2)
        else:
            login_user(check_login)
            return redirect('/')
    return redirect('/')

@login_pages.route('/login/')
def login():
    return render_template('login.html')
