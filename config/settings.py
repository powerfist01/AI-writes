from dotenv import load_dotenv
load_dotenv()

# Path: config/settings.py

import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

BCC_MAIL = os.getenv('BCC_MAIL')

MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_FROM_ADDRESS = os.getenv('MAIL_FROM_ADDRESS')

MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')