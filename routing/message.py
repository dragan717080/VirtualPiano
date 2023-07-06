from flask import render_template, request, redirect, Blueprint
from flask_cors import cross_origin
from flask_login import login_required, current_user
from db_models import User, Message

message_pages = Blueprint('message', __name__)

@message_pages.route('/compose-message', methods = ['POST'])
@login_required
def compose_message_post():
    if request.form['submit'] == 'compose-message':
        recipient_username = request.form['compose-message']
        recipient = User.get(username=recipient_username)
        message_content = request.form['message_content']
        if message_content != '' and len(User.query.filter_by(username = recipient_username).all()) > 0 and recipient_username != current_user.username:
            message = Message(content = message_content, author = User.get(username = current_user.username), recipient = recipient)
            message.save()
            return redirect('/')
        else:
            errors = []
            if message_content == '':
                errors.append('Message content must not be empty')
            if len(User.query.filter_by(username = recipient_username).all()) == 0:
                errors.append("Username doesn't exist")
            if recipient_username == current_user.username:
                errors.append('Sending self message')
            return render_template('compose-message.html', loggedinuser = current_user.username, errors = errors, recipient = request.args.get('recipient'))

@message_pages.route('/compose-message')
@cross_origin()
def compose_message():
    return render_template('compose-message.html', loggedinuser = current_user.username, recipient = request.args.get('recipient'))
