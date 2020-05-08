from urlshort import create_app
from urlshort.models import db
from urlshort.strings import Strings

app = create_app()


@app.cli.command()
def createdb():
    db.create_all()
