import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "your@gmail.com"
receiver_email = "receiver@example.com"
password = "Password"  # Use App Password if 2FA is enabled

# Create email content
message = MIMEMultipart("alternative")
message["Subject"] = "Automated Reminder"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
This is an automated reminder from Python script.
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       This is  <b>Sultan Ali</b> from Pakistan.<br> 
       Just let you know that all the projects you have selected are complete successfully.

    </p>
  </body>
</html>
"""

# Add plain-text and HTML to email
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Send the email
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent!")
