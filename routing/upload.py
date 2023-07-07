from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from flask_cors import cross_origin
from flask_login import login_required, current_user
from db_models import MusicSheet
from helpers import Helpers

upload_pages = Blueprint('upload', __name__)

@upload_pages.route('/upload', methods = ['POST'])
@cross_origin()
@login_required
def upload_post():
    if request.form['submit'] == 'upload-music':
        uploaded_sheet = request.files['upload-music']
        uploaded_sheet_title = uploaded_sheet.filename
        if uploaded_sheet_title != '':
            sheet_params = {
                'content': uploaded_sheet.read().decode('utf-8'),
                'author_id': current_user.id
            }
            
            artist_name = uploaded_sheet_title.split(' - ')[0]
            # Artist is unknown
            if '.' in artist_name:MusicSheet(
                title = uploaded_sheet_title.split('.txt')[0], **sheet_params).save()
            else:
                Helpers.save_sheet_with_known_artist(uploaded_sheet_title, artist_name, sheet_params)

            return redirect(request.url)
        else:
            return redirect(request.url)

@upload_pages.route('/upload')
@cross_origin()
@login_required
def upload():
    return render_template('upload.html', loggedinuser = current_user.username, admin = current_user.is_admin)