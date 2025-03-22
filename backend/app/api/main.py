from fastapi import APIRouter

from backend.app.api.routes import login

api_router = APIRouter()
api_router.include_router(login.router)
