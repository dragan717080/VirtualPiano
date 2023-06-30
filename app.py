from routing.routes import index_pages
from create_app import create_app
from config.assets_config import configure_assets

app = create_app()
configure_assets(app)

app.register_blueprint(index_pages)

if __name__ == '__main__':
    app.run(debug = True)
