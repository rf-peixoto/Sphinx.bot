import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -------------------------------------------- #
class MailSender:

    def __init__(self):
        self.sender = "YOUR BOT EMAIL"
        self.sender_password = "YOUR BOT EMAIL PASSWORLD"
        self.mail_subject = "EMAIL SUBJECT"

    def send_email(self, recipient, token):
        # Template:
        message = """This is your removal token: {0}

Enter the command below on the platform where the request was made:

.verify {0}

PLEASE: DO NOT RESPOND TO THIS MESSAGE.""".format(token)
        email = MIMEMultipart()
        email['From'] = self.sender
        email['To'] = recipient
        email['Subject'] = self.mail_subject
        email.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.sender_password)
        server.sendmail(self.sender, recipient, email.as_string())
        server.quit()
        return
