from flask import Flask

from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from urlshort.models import db

    db.init_app(app)

    from urlshort.routes import shortener

    app.register_blueprint(shortener)
    with app.app_context():
        db.create_all()

    return app
