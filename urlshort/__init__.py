from flask import Flask, render_template, session, request, flash, url_for, redirect, Response, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os

from urlshort.strings import Strings

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    app.app_context().push()
    return app


def create_test_app(self):
    app = Flask(__name__)
    app.config.update(
        TESTING=True,
        SECRET_KEY="testingsecretkey!?!",
        SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        URL="urlshort.git"
    )
    db.init_app(app)
    app.app_context().push()
    return app

