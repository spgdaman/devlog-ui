from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap =Bootstrap()


def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # Initialize Flask Extensions
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config

    return app