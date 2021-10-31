import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re


class Mail():
    def __init__(self, receiver_email='gaurav.mishra.cx@gmail.com', subject='Error Mail', nonHtmlFlag=False):
        """

        :param receiver_email: accepts string with proper formatted mail address of sender
        :param subject: string for subject part of email by default it is set to be blank quotes
        :param body: Triple quoted string for body portion of email by default it is set to be blank quotes
        :param nonHtmlFlag: sets body type from html to plain default False
        :returns: Returns True if everything goes right else will either raise error or return false

        """

        super().__init__()
        self.to_mail = receiver_email
        self.subject = subject
        self.body = None
        self.server_started = False

        self.msg = None
        self.regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
        self.mi_type = 'html' if not nonHtmlFlag else 'plain'

    def send_email(self, body=''):
        try:
            self.body = body
            # =======================================================================

            sender_email = self.conf.get('SMTP_EMAIL_ID')
            server_id = self.conf.get('SMTP_SERVER_ID')
            password = self.conf.get('SMTP_PASSWORD')

            # =======================================================================

            self._mail_validation()
            self.msg = MIMEMultipart()
            self.msg["From"] = sender_email
            self.msg["Bcc"] = self.conf.get('WE_SERVE_DEV_MAIL_ID')
            self.msg["To"] = self.to_mail.lower()
            self.msg["Subject"] = self.subject

            self.msg.attach(MIMEText(self.body, self.mi_type))
            text = self.msg.as_string()

            self.server_started = True
            with smtplib.SMTP_SSL(server_id, 465) as server:
                print(server.ehlo())
                server.login(sender_email, password)
                if self.conf.get('MAIL_FLAG'):
                    server.sendmail(sender_email, self.to_mail, text)

        except smtplib.SMTPAuthenticationError as e:
            print(e)
            raise PermissionError('Incorrect Password Provided')

        except BaseException as B:
            raise B
        finally:
            if self.server_started:
                server.close()
            else:
                pass

    def _mail_validation(self):
        try:
            if not re.search(self.regex, self.to_mail):
                raise Exception('Email Address {} Invalid'.format(self.to_mail))
            if not self.to_mail:
                raise Exception('Email Address Is Required')

            return True

        except BaseException as B:
            raise B


if __name__ == '__main__':
    print(Mail(receiver_email='gm150180107025@gmial.com').send_email())
