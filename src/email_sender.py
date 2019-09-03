import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SenderProp:
    PORT = 25
    SMTP_SERVER = "smtp.live.com"#server for hotmail
    SENDER_EMAIL = "your email"
    PASSWORD = "your password"

class Email(SenderProp):
    def __init__(self, receiver):

        self._receiver_email = receiver
        self._message = MIMEMultipart("alternative")
        self._message["From"] = self.SENDER_EMAIL
        self._message["To"] = receiver

    def send(self, subject, messaggio):
        self._message["Subject"] = subject
        context = ssl.create_default_context()
        part1 = MIMEText(messaggio, "plain")
        self._message.attach(part1)
        with smtplib.SMTP(self.SMTP_SERVER, self.PORT) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.SENDER_EMAIL, self.PASSWORD)
            server.sendmail(self.SENDER_EMAIL, self._receiver_email, self._message.as_string())
