import email
import imaplib
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class MailOperations:
    def __init__(self, email, password):
        self.portSSL = 465
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = email
        self.password = password

    def send_email(self, receiver_email, subject, text, files_list):

        msg = MIMEMultipart()
        msg['Subject'] = subject


        msg.attach(MIMEText(text, 'plain'))

        for file in files_list:

            filename = os.path.basename(file)
            attachment = open(file, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)


        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.sender_email, self.password)
        print("Login successful")
        text = msg.as_string()
        s.sendmail(self.sender_email, receiver_email, text)
        print("Message sent")
        s.quit()

    def readMail(self):
        EMAIL = self.sender_email
        PASSWORD = self.password
        SERVER = 'imap.gmail.com'
        x = "                      Inbox messages: " + self.sender_email + " "


        mail = imaplib.IMAP4_SSL(SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select('inbox')

        status, data = mail.search(None, 'ALL')
        #print(data)
        mail_ids = []

        for block in data:
            mail_ids += block.split()
            #print(mail_ids)

        for i in mail_ids:

            status, data = mail.fetch(i, '(RFC822)')

            # '(RFC822)'-- tuple
            for response_part in data:
                #print(response_part)
                if isinstance(response_part, tuple):

                    message = email.message_from_bytes(response_part[1])

                    mail_from = message['from']
                    mail_subject = message['subject']


                    if message.is_multipart():
                        mail_content = ''

                        for part in message.get_payload():

                            if part.get_content_type() == 'text/plain':
                                mail_content += part.get_payload()
                    else:

                        mail_content = message.get_payload()

                    x += "\n\n"
                    x += mail_from
                    x += "\n\n"
                    x += mail_subject
                    x += "\n\n"
                    x += mail_content
                    x += "\n"
                    x += "=============================================================================="

        # print(x)
        return x
