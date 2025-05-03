from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.app.models import *
from backend.app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter_by(nickname=user.nickname).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Nickname already taken")

    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        nickname=user.nickname,
        password=hashed_password,
        status_id="offline"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
