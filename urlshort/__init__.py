from flask import Flask

from config import Config, TestConfig
from urlshort.models import db


def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(Config)

    db.init_app(app)

    from urlshort.routes import shortener

    app.register_blueprint(shortener)
    with app.app_context():
        db.create_all()

    app.shell_context_processor(shell_context)

    return app


def shell_context():
    """Shell context objects."""
    return {"db": db}
