import random

from flask import (
    Flask, render_template
)

from flask_wtf import FlaskForm
from flask_pagedown import PageDown
from wtforms import StringField, SubmitField, validators
from app.gemini_pro import GeminiPro

app = Flask(__name__)
pagedown = PageDown(app)

app.secret_key = str(random.randint(1, 20))

class EnterEmailForm(FlaskForm):
    email = StringField('Email*', validators=[validators.InputRequired("Please enter your email"), validators.Email('Email format incorrect')])
    submit = SubmitField('Send me an AI-Generated story!')

@app.route('/', methods=['GET', 'POST'])
def home_page():
    '''
        App for hompage
    '''
    
    form = EnterEmailForm()
    if form.validate_on_submit():

        # gemini = GeminiPro()
        # story = gemini.generate_story_using_prompt()

        form.email.success = ['Your story is brewing! We will send you an email once the AI-generated story is cooked.']
        return render_template('homepage.html', form=form)
    
    return render_template('homepage.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
