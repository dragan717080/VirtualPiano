from flask_assets import Environment, Bundle

def create_bundle(input_file, output_file=None):

    if output_file is None:
        output_file = input_file

    bundle = Bundle(
        f'scss/{input_file}.scss',
        filters=['libsass'],
        output=f'dist/css/{output_file}.css',
        depends='scss/*.scss'
    )

    return bundle

def configure_music_assets(assets):

    music_sheets_css = create_bundle('music/sheets')

    assets.register('sheets_css', music_sheets_css)

def configure_assets(app):
    assets = Environment(app)

    bundle_names = ['base_css', 'index_css', 'register_css', 'profile_css', 
        'login_css', 'upload_css', 'inbox_css']
    bundles = {name: create_bundle(name.split('_')[0]) for name in bundle_names}

    for bundle_name, bundle_obj in bundles.items():
        assets.register(bundle_name, bundle_obj)
        bundle_obj.build()

    configure_music_assets(assets)
