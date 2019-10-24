from flask_sqlalchemy import SQLAlchemy
from urlshort import app, db
from datetime import datetime

class Link(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    long = db.Column(db.String())
    short = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return '<Link {}: {} >'.format(self.id, self.timestamp)

    

