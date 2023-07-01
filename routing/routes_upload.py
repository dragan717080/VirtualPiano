from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from config.log_config import logging
import time
import os
from db_models import MusicSheet

upload_pages = Blueprint('upload', __name__)

@upload_pages.route('/upload', methods = ['POST'])
@cross_origin()
@login_required
def upload_post():
    if request.method == 'POST':
        if request.form['submit'] == 'upload-music':
            uploaded_sheet = request.files['upload-music']
            uploaded_sheet_title = uploaded_sheet.filename
            if uploaded_sheet_title != '':
                sheet_params = {
                    'title': uploaded_sheet_title,
                    'content': uploaded_sheet.read().decode('utf-8'),
                    'author_id': current_user.id
                }
                sheet = MusicSheet(**sheet_params)
                sheet.save()
                return redirect(request.url)
            else:
                return redirect(request.url)

@upload_pages.route('/upload')
@cross_origin()
@login_required
def upload():
    return render_template('upload.html', loggedinuser = current_user.username, admin = current_user.is_admin)