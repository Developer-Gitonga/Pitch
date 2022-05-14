import os
from config import Config, config_options
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .models import User
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    from .main import main as mainblueprint
    app.register_blueprint(mainblueprint)

    return app
