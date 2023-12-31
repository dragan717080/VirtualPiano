from flask import render_template, request, redirect, Blueprint
from flask_login import login_required, current_user
from config.log_config import logging
from db_models import db, Comment, MusicSheet, Artist
from helpers import Helpers

music_pages = Blueprint('music', __name__, template_folder='templates/music/', url_prefix = '/music')

@music_pages.route('/', methods = ['POST'])
def music_post():
    if request.form['submit'] == 'POST SONG REQUEST':
        song_request = Comment(content = request.form['song_request'], author_id = current_user.id)
        song_request.save()
        return redirect(request.url)

@music_pages.route('/')
def music():
    data = Helpers.read_json_file('music_data')
    params = {
        'comments': Comment.query.all(),
        'latest_sheets': MusicSheet.get_latest(),
        'data': data
    }
    if current_user.is_anonymous:
        return render_template('/music/sheets.html', **params)
    
    params.update({
        'loggedinuser': current_user.username,
        'avatar': current_user.avatar.image if current_user.avatar is not None else None,
        'avatar_format': current_user.avatar.image_format if current_user.avatar is not None else None,
        'admin': current_user.is_admin,
    })
    return render_template('/music/sheets.html', **params)

@music_pages.route('/genres')
def genres():
    if current_user.is_anonymous:
        return render_template('music/genres.html')
    return render_template('music/genres.html', loggedinuser = current_user.username, admin = current_user.isadmin)

@music_pages.route('/genres/<string:genre>')
def sheets_genre(genre):
    if current_user.is_anonymous:
        return render_template('music/genre.html', genre = genre, music_sheets_for_genre = get_music_sheets_for_genre(genre))
    return render_template('music/genre.html', loggedinuser = current_user.username, genre = genre, music_sheets_for_genre = get_music_sheets_for_genre(genre), admin = current_user.isadmin)

@music_pages.route('/sort_genres/', methods = ['GET', 'POST'])
@login_required
def sort_genres():
    #admins sort out genres of existing sheets
    music_sheets = []
    for i in range(len(MusicSheet.query.all())):
        dict1 = vars(MusicSheet.query.all()[i])
        music_sheets.append(dict1)
    return render_template('music/sort_genres.html', music_sheets = music_sheets, loggedinuser = current_user.username, admin = is_admin(current_user.username))

@music_pages.route('/artists')
def artists():
    letter = request.args.get('letter')
    music_artists = Artist.get_by_letter('name', letter)
    if current_user.is_anonymous:
        return render_template('music/artists.html', letter = letter, music_artists = music_artists)
    return render_template('music/artists.html', loggedinuser = current_user.username, letter=letter,
        music_artists=music_artists)

@music_pages.route('/artists/<int:id>')
def artist(id):
    artist = Artist.get_by_id(id)
    if current_user.is_anonymous:
        return render_template('music/artist.html', artist = artist)
    
    return render_template('music/artist.html', loggedinuser = current_user.username, artist = artist)

@music_pages.route('/sheets')
def sheets():
    data = Helpers.read_json_file('music_data')
    letter = request.args.get('letter')
    music_sheets = MusicSheet.get_by_letter('title', letter)
    print(music_sheets)
    params = {
        'letter': letter, 'music_sheets': music_sheets, 'data': data
    }

    if current_user.is_anonymous:
        return render_template('music/sheets.html', **params)
    return render_template('music/sheets.html', loggedinuser = current_user.username, **params)

@music_pages.route('/sheets/<int:id>')
def sheet_by_id(id):
    music_sheet = MusicSheet.get_by_id(id)
    if current_user.is_anonymous:
        return render_template('music/sheet.html', music_sheet = music_sheet)
    
    return render_template('music/sheet.html', loggedinuser = current_user.username, music_sheet = music_sheet)
