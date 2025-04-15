from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse
import aiosmtplib
from email.message import EmailMessage
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

GMAIL_USER = "nebulacore.inc@gmail.com"
GMAIL_APP_PASSWORD = "your_app_password"

class Message(BaseModel):
    name: str
    email: EmailStr | None = None
    subject: str | None = None
    message: str | None = None

origins = [
    "https://shovickbarua.info",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send-message")
async def send_message(data: Message):
    try:
        message = EmailMessage()
        message["From"] = GMAIL_USER
        message["To"] = GMAIL_USER  # or any recipient
        message["Subject"] = data.subject
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
        )

        return JSONResponse(content={"message": "Email sent successfully!"}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)