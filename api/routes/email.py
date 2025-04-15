from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Message
from services.email_service import send_email
from config import GMAIL_USER, GMAIL_APP_PASSWORD
router = APIRouter()

@router.post("/send-message")
async def send_message(data: Message):
    try:
        await send_email(data)
        return JSONResponse(content={"message": "Email sent successfully!"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# @router.post("/send-message")
# async def send_message(data: Message):
#     try:
#         await send_email(data)
#         return JSONResponse(
#             content={
#                 "message": "Email sent successfully!",
#                 "debug": {
#                     "GMAIL_USER": GMAIL_USER,
#                     "GMAIL_APP_PASSWORD": GMAIL_APP_PASSWORD  # ⚠️ Only for testing
#                 }
#             },
#             status_code=200
#         )
#     except Exception as e:
#         # Include GMAIL_USER and GMAIL_APP_PASSWORD in the error response (for debugging)
#         return JSONResponse(
#             content={
#                 "error": str(e),
#                 "debug": {
#                     "GMAIL_USER": GMAIL_USER,  # ⚠️ Only for testing
#                     "GMAIL_APP_PASSWORD": GMAIL_APP_PASSWORD  # ⚠️ Only for testing
#                 }
#             },
#             status_code=500
#         )
