import os

from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_BCC = os.getenv('MAIL_BCC')

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')