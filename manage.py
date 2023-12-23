from flask_pagedown import PageDown
from flask import Flask, render_template, request

import services.settings as settings
from services.worker import celery
from services.forms import EnterEmailForm

app = Flask(__name__)
pagedown = PageDown(app)

app.secret_key = settings.APP_SECRET

@app.route('/', methods=['GET', 'POST'])
def home_page():
    '''
        App for hompage
    '''
    
    form = EnterEmailForm()
    if request.method == 'POST' and form.validate():
    
        client_email = request.form['email']
    
        task = celery.send_task('tasks.send_enchanting_story_to_user', args=[client_email], kwargs={})
        form.email.task_id = task.id

        form.email.success = ['Your story is brewing! We will send you an email once the AI-generated story is cooked.']
        return render_template('homepage.html', form=form)
    
    return render_template('homepage.html', form=form)
