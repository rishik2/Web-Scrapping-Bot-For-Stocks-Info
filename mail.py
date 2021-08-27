import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def sending_email(filename):
    subject = 'Stock Reports For Today'

# For sending email with from, to and body
    msg = MIMEMultipart()
    msg['From'] = 'beingawriter92@gmail.com'
    msg['To'] = 'poodleintherut@gmail.com'
    msg['Subject'] = subject

    body = 'Financial reports for today are attached with the mail'


    msg.attach(MIMEText(body, 'plain'))

# For sending csv attachment
    file_attach = open(filename , 'rb' )
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(file_attach.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename = ' + filename )
    msg.attach(part)

# coverting all the data stored inside msg as string
    message = msg.as_string()

#using smtp connection with google server to send the mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('beingawriter92@gmail.com', 'isyvibnsgyigwgfl')

    mail_from = 'beingawriter92@gmail.com'
    mail_to = 'poodleintherut@gmail.com'


    server.sendmail(mail_from,mail_to, message)

    server.quit()

