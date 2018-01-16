import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Configures weather_app and enables hidden-tag option for flashes.
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "this-not-encrypted-yet"

    # Creates connection to local database
    DB_URL = 'postgresql://{user}:{pw}@{url}/{dab}'.format(
        user='postgres', pw='kirby_89', url='localhost', dab='weatherdb')
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

