from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class EnterEmailForm(FlaskForm):
    email = StringField('Email*', validators=[validators.InputRequired("Please enter your email"), validators.Email('Email format incorrect')])
    submit = SubmitField('Send me an AI-Generated story!')
