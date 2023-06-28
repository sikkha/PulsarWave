from email.mime.multipart import MIMEMultipart
import sys
import argparse

# Set up the SMTP connection
smtp_host = 'smtp.sendgrid.net'
smtp_port = 587
smtp_username = 'apikey'
smtp_password = 'YOUR_SENDGRID_PASSWORD'

# Create a parser and add arguments
parser = argparse.ArgumentParser(description='Send an email.')
parser.add_argument('subject', help='The subject of the email')

# Parse the command line arguments
args = parser.parse_args()

# Create the email message
sender_email = 'yourmail@yourdomain.com'
receiver_emails = ['mail1@yourdomain.com', 'mail2@yourdomain.com']  # List of recipients
subject = args.subject  # Use the subject from the command line arguments
message = sys.stdin.read().strip()

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_emails)  # Join the list with a comma
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Open the SMTP connection
smtp_connection = smtplib.SMTP(smtp_host, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Send the email
smtp_connection.sendmail(sender_email, receiver_emails, msg.as_string())
smtp_connection.quit()

print("Email sent successfully!")

