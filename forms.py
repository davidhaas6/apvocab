from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired


class SearchForm(Form):
    term = StringField('Search term', validators=[InputRequired()])
