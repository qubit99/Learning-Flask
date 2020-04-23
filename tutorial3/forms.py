# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of the puppy : ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Id no of the puppy to remove : ')
    submit = SubmitField('Remove Puppy')

class OwnerForm(FlaskForm):
    name = StringField('Name of the owner')
    id = IntegerField('Puppy id')
    submit = SubmitField('Add Owner')

