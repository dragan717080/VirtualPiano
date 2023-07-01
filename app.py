from routing.routes import index_pages
from routing.routes_register import register_pages
from routing.routes_login import login_pages
from routing.routes_logout import logout_pages
from routing.routes_profile import profile_pages
from routing.routes_upload import upload_pages
from create_app import create_app
from config.assets_config import configure_assets

app = create_app()
configure_assets(app)

app.register_blueprint(index_pages)
app.register_blueprint(register_pages)
app.register_blueprint(login_pages)
app.register_blueprint(logout_pages)
app.register_blueprint(profile_pages)
app.register_blueprint(upload_pages)

if __name__ == '__main__':
    app.run(debug = True)
