from fastapi import APIRouter

from .routes import card, router, auth

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(card.router)
api_router.include_router(router.router)


