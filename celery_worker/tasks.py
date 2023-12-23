import os
from celery import Celery

import config.settings as settings

from gemini_pro import GeminiPro
from mailer import Mailer

celery = Celery('tasks', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

@celery.task(name='tasks.send_enchanting_story_to_user')
def send_enchanting_story_to_user(client_email: str):
    '''
        Generate story and send to client
    '''

    subject = 'Your AI-Crafted Tale Is Ready!'

    gemini = GeminiPro()
    content = gemini.generate_story_using_prompt()

    if(not content):
        return {
            'status': 'error',
            'message': 'Gemini Pro failed to generate story'
        }

    mailer = Mailer()
    mailer.send_client_email(subject, content, client_email)
    
    return {
        'status': 'success',
        'message': 'Email sent successfully'
    }