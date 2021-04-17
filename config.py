from os import environ, path
from datetime import timedelta
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    JWT_AUTH_HEADER_PREFIX = environ.get("JWT_AUTH_HEADER_PREFIX")
    JWT_EXPIRATION_DELTA = timedelta(seconds=int(environ.get("JWT_EXPIRATION_DELTA")))
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False