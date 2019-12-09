import smtplib
import ssl
import base64
import configparser 

class Chaldea(object):

    def __init__(self, *args, **kawgs):
        self.config = configparser.ConfigParser()
        self.config.read('configuration.ini')
        self.smtp_server = self.config['connection']['server']
        self.port = self.config['connection']['port']
        self.user = self.config['credentials']['user']
        self.password = self.config['credentials']['password']
        self.recipient = {_ for _ in args}

    def send_message(self, message:str):
        """Connects to smtp server to send notification, alarms, and analysis reports."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as self.server:
            self.server.login(self.user, password)
            self.server.sendmail(self.user, self.recipient, message)
