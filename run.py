from flask import current_app

from urlshort import create_app, Strings, db

app = create_app()


@current_app.shell_context_processor
def make_shell_context():
    return {'db': db}


@current_app.context_processor
def inject_strings():
    """
    Inject strings automatically into the context of templates
    """
    return Strings.strings
