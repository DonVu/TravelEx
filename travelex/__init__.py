import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'travelex.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/')
    def main_page():
        return 'Main Page'
    
    @app.route('/flights')
    def flights():
        return 'Flights page'

    @app.route('/hotels')
    def hotels():
        return 'Hotels page'

    @app.route('/events')
    def events():
        return 'Events page'

    @app.route('/suggestions')
    def suggestions():
        return 'Suggestions page'

    return app
