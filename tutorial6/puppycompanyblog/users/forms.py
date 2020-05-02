from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_conf', message='Passwords must match!')])
    password_conf = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter(email = field.data).first():
            raise ValidationError('Your email has been registered already!')
    
    def check_username(self, field):
        if User.query.filter(username=field.data).first():
            raise ValidationError('Your username has been registered already!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Upload profile picture', validators = [FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        if User.query.filter(username=field.data).first():
            raise ValidationError('Your username has been registered already!')
