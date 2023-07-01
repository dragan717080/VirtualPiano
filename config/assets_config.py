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

def configure_assets(app):
    assets = Environment(app)

    css = create_bundle('base')
    index_css = create_bundle('index')
    register_css = create_bundle('register')
    profile_css = create_bundle('profile')
    login_css = create_bundle('login')

    assets.register('asset_css', css)
    assets.register('index_css', index_css)
    assets.register('register_css', register_css)
    assets.register('profile_css', profile_css)
    assets.register('login_css', login_css)

    css.build()
    index_css.build()
