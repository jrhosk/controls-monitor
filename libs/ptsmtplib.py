import smtplib
import ssl
import base64

class Chaldea(object):

    def __init__(self, *args, **kawgs):
        self.smtp_server = 'smtp.gmail.com'
        self.port = 465     # For SSL
        self.sender = 'e1039spinquest@gmail.com'
        self.recipient = {_ for _ in args}


    def send_message(self, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as self.server:
            self.server.login(self.sender, '')
            self.server.sendmail(self.sender, self.recipient, message)
