import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


def send_email(receiver_email, subject, body):
    try:
        message = MIMEMultipart()

        message["From"] = Config.EMAIL
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(
            Config.EMAIL,
            Config.EMAIL_PASSWORD
        )

        server.sendmail(
            Config.EMAIL,
            receiver_email,
            message.as_string()
        )

        server.quit()

        return True

    except Exception as e:
        print("Email Error:", e)
        return False