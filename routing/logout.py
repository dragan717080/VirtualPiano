from flask import redirect, Blueprint, flash
from flask_login import logout_user, current_user

logout_pages = Blueprint('logout', __name__)

@logout_pages.route('/logout')
def logout():
    user = current_user.username
    logout_user()
    flash(f'User {user} has been successfully logged out.')
    return redirect('/')
