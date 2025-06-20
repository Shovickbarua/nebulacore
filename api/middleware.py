from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import ALLOWED_ORIGINS

def setup_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
