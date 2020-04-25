# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of the owner')
    id = IntegerField('Puppy id')
    submit = SubmitField('Add Owner')
