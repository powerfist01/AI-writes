import smtplib

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config.settings as settings

class Mailer:

    def send_client_email(self, subject, content, client_email):

        email_parameters = {
            'subject': subject,
            'content': content,
            'to': [client_email],
            'bcc': [settings.BCC_MAIL],
        }
        self.__send_email(email_parameters)

    def __send_email(self, email_parameters):

        server = smtplib.SMTP_SSL(settings.MAIL_HOST, 465)
        server.login(settings.MAIL_FROM_ADDRESS, settings.MAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['Subject'] = email_parameters["subject"]
        msg['From'] = formataddr(('Story AI', settings.MAIL_FROM_ADDRESS))

        to = email_parameters.get('to', [])
        bcc = email_parameters.get('bcc', [])
        msg['To'] = ', '.join(to)

        html = email_parameters['content']
        part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')
        msg.attach(part2)

        server.sendmail(settings.MAIL_FROM_ADDRESS, to + bcc, msg.as_string())
