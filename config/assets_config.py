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

    assets.register('asset_css', css)
    assets.register('index_css', index_css)

    css.build()
    index_css.build()
