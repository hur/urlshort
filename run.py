from urlshort import app, db
from urlshort.strings import Strings


@app.shell_context_processor
def make_shell_context():
    return {'db': db}


@app.context_processor
def inject_strings():
    """
    Inject strings automatically into the context of templates
    """
    return Strings.strings
