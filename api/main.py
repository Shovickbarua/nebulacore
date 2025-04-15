from fastapi import FastAPI
from middleware import setup_middleware
from routes.email import router as email_router

app = FastAPI()

setup_middleware(app)

app.include_router(email_router)
