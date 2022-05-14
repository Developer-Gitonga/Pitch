import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    DEBUG = True

    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
