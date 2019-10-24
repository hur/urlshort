from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired, URL


class URLForm(FlaskForm): 
    url = StringField('url', validators=[DataRequired(), URL(require_tld=True)],
                     render_kw={"placeholder": "Paste URL here"})