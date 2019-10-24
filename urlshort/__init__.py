from flask import Flask, render_template, session, request, flash, url_for, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from urlshort import routes, models