import email, smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
date = datetime.now().strftime("%m-%d-%Y")
sender_email = ""
password = ""
receiver_email = ""
message = MIMEMultipart("alternative")
message["Subject"] = "Crypto analysis " + date
message["From"] = sender_email
message["To"] = receiver_email

# write the HTML part
html = """\
<html>
<body>
<img src="cid:Mailtrapimage1">
<img src="cid:Mailtrapimage2">
</body>
</html>
"""

part = MIMEText(html, "html")
message.attach(part)

# We assume that the image file is in the same directory that you run your Python script from
fp = open('images/most_mentioned_picks_' + date + '.png', 'rb')
image = MIMEImage(fp.read())
fp.close()

# Specify the ID according to the img src in the HTML part
image.add_header('Content-ID', '<Mailtrapimage1>')
image.add_header(
    "Content-Disposition",
    f"attachment; filename= {'most_mentioned_picks_' + date + '.png'}",
)
message.attach(image)

# We assume that the image file is in the same directory that you run your Python script from
fp = open('images/sentiment_analysis_' + date + '.png', 'rb')
image = MIMEImage(fp.read())
fp.close()

# Specify the ID according to the img src in the HTML part
image.add_header('Content-ID', '<Mailtrapimage2>')
image.add_header(
    "Content-Disposition",
    f"attachment; filename= {'sentiment_analysis_' + date + '.png'}",
)
message.attach(image)

# Open PDF file in binary mode
with open('logs/analysis_log_' + date + '.txt', "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {'analysis_log_' + date + '.txt'}",
)

# Add attachment to message and convert message to string
message.attach(part)

port = 465
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
    sender_email, receiver_email, message.as_string()
    )

print('Sent email')