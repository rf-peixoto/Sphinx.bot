import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -------------------------------------------- #
class MailSender:

    def __init__(self):
        self.sender = "YOUR EMAIL"
        self.sender_password = "YOUR PASSWORD"
        self.mail_subject = "Your BOT Token"
        print("Connecting to email server. This could take a while.")
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender, self.sender_password)
        print("Email manager ready.")

    def send_email(self, recipient, token):
        message = """This is your removal token: {0}

Enter the command below on the platform where the request was made:

.verify {0}

If you did not request this email, please ignore it.
PLEASE DO NOT RESPOND TO THIS MESSAGE.""".format(token)
        #print("Creating message.") # DEBUG
        email = MIMEMultipart()
        email['From'] = self.sender
        email['To'] = recipient
        email['Subject'] = self.mail_subject
        email.attach(MIMEText(message, 'plain'))
        
        #print("Sending...") # DEBUG
        self.server.sendmail(self.sender, recipient, email.as_string())
        #server.quit()

        return
