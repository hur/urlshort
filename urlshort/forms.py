from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL, InputRequired


class URLForm(FlaskForm):
    url = StringField('url', validators=[InputRequired(), URL(require_tld=True)],
                      render_kw={"placeholder": "Paste URL here",
                                 "onfocus": "this.placeholder = ''",
                                 "onblur": "this.placeholder = 'Paste URL here'"
                                 })


class UnshortenForm(FlaskForm):
    url = StringField('url', validators=[InputRequired()],
                      render_kw={"placeholder": "Enter URL to unshorten",
                                 "onfocus": "this.placeholder = ''",
                                 "onblur": "this.placeholder = 'Enter URL to unshorten'"
                                 })
