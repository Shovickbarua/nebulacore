from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    name: str
    email: EmailStr | None = None
    subject: str | None = None
    message: str | None = None
