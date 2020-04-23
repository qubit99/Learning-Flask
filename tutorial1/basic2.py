from flask import Flask, flash, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import (BooleanField, StringField, PasswordField, validators, TextAreaField,
                        RadioField, DateTimeField, SelectField, TextField, SubmitField )
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY']  = "mykey"

class InfoForm(FlaskForm):
    breed = StringField('What breed are you', validators = [DataRequired()])
    neutered = BooleanField('Have you been neurered')
    mood = RadioField('What is your current mood?', choices = [('mood_one', 'Happy'), ('mood_two', 'excited')])
    food_choice = SelectField('Select your fav food', choices = [('chicken', 'chicken'), ('fish', 'fish'), ('beef', 'beef')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        flash('You just clicked a button')
        return redirect(url_for('index'))

    return render_template('index.html', form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug = True)
    


