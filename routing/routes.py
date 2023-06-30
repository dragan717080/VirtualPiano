from flask import render_template, Blueprint

index_pages = Blueprint('index', __name__,
    template_folder='templates', static_folder='static', url_prefix='/')

@index_pages.route('/')
def index():
    return render_template('index.html')
