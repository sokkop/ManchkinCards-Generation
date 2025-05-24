from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..models import User
from ..schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Добавление нового пользователя
def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.login, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Получение пользователя по имени
def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()
