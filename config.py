import os
import uuid

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'urlshort.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    URL = "urlshort.git"


class TestConfig(object):
    SECRET_KEY = str(uuid.uuid4().hex)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    URL = "urlshort.git"
    TESTING = True
    WTF_CSRF_ENABLED = False
