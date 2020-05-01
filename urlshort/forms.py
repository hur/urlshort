from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import URL, InputRequired


class URLForm(FlaskForm):
    url = StringField('url', validators=[InputRequired(), URL(require_tld=True)],
                      render_kw={"placeholder": "Paste URL here"})


class UnshortenForm(FlaskForm):
    url = StringField('url', validators=[InputRequired()],  # ADD URL
                      render_kw={"placeholder": "Enter URL to unshorten"})
