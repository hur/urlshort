from flask import current_app

from urlshort import Strings


@current_app.context_processor
def inject_strings():
    """
    Inject strings automatically into the context of templates
    """
    return Strings.strings