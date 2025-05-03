from sqlalchemy.orm import Session
from backend.app.models import *
from passlib.context import CryptContext

from backend.app.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_user(db: Session, user_create: UserCreate):
    hashed_password = get_password_hash(user_create.password)

    # Можно назначать дефолтный статус_id = 1 (например "обычный пользователь")
    db_user = User(
        nickname=user_create.nickname,
        password=hashed_password,
        status_id=1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
