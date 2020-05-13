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
    URL = os.environ.get('URL') or 'URL NOT SET'
    PROTOCOL = os.environ.get('URLSHORT_PROTOCOL') or 'http://'


class TestConfig(object):
    SECRET_KEY = str(uuid.uuid4().hex)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    URL = "http://127.0.0.1:5000"
    TESTING = True
    WTF_CSRF_ENABLED = False
    PROTOCOL = 'http://'
