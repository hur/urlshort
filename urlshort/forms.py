from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired


class URLForm(FlaskForm): 
    url = StringField('url', validators=[DataRequired()],
                     render_kw={"placeholder": "Paste URL here"})