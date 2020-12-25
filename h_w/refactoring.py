import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class WorkWithEmail:
    def __init__(self, gmail_s_m_p_t="smtp.gmail.com", gmail_i_m_a_p="imap.gmail.com", my_login='login@gmail.com',
                 password='qwerty', subject='Subject', recipients=('vasya@email.com', 'petya@email.com'),
                 message='Message', header=None):
        self.GMAIL_SMTP = gmail_s_m_p_t
        self.GMAIL_IMAP = gmail_i_m_a_p
        self.my_login = my_login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header

    def send_message(self):
        my_message = MIMEMultipart()
        my_message['From'] = self.my_login
        my_message['To'] = ', '.join(self.recipients)
        my_message['Subject'] = self.subject
        my_message.attach(MIMEText(self.message))

        server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client # идентифицировать себя SMTP-клиенту Gmail
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()

        server.login(self.my_login, self.password)
        server.sendmail(self.my_login, server, my_message.as_string())

        server.quit()

    def receive(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.my_login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    experimental = WorkWithEmail()
    experimental.send_message()
    experimental.receive()
