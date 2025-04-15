import aiosmtplib
from email.message import EmailMessage
from models import Message
from config import GMAIL_USER, GMAIL_APP_PASSWORD
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def send_email(data: Message):
    message = EmailMessage()
    message["From"] = GMAIL_USER
    message["To"] = GMAIL_USER  # or any recipient
    message["Subject"] = data.subject or "No Subject"
    message.set_content(
        f"Name: {data.name}\nEmail: {data.email}\nMessage:\n{data.message}"
    )

    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username=GMAIL_USER,
        password=GMAIL_APP_PASSWORD,
        tls_context=ssl_context,
    )
