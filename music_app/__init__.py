from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from music_app.config import Config

# Create Bcrypt object for password encryption
bcrypt = Bcrypt()

# Create db object for SQLAlchemy ORM
db = SQLAlchemy()

# Create login manager to handle user sessions
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config=Config):
    """
    This function is used for app creation with the
    configurations passed to it

    :param config:  Config class with all the configuration
    :return:        reurn a flask application
    """

    # Create flask application
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initiate the extensions for the app
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    # Import the blueprints from the project modules
    from music_app.users.routes import users
    from music_app.songs.routes import songs
    from music_app.albums.routes import albums
    from music_app.artists.routes import artists
    from music_app.index.routes import index

    # Register the blueprints of the modules with the app
    app.register_blueprint(users)
    app.register_blueprint(songs)
    app.register_blueprint(albums)
    app.register_blueprint(artists)
    app.register_blueprint(index)

    # Return app
    return app