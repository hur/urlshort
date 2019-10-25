from flask import Flask, render_template, session, request, flash, url_for, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from urlshort import routes, models

# Logfiles
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    handler = RotatingFileHandler('logs/urlshort.log', maxBytes=10240, backupCount=10)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Startup.')



    