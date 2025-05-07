from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.storage.postgres import get_db
from backend.app.schemas.user import UserCreate
from backend.app.services import auth_service

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register_user(db, user)
