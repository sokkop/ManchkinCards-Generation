from sqlalchemy.orm import Session
from passlib.context import CryptContext

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate
from backend.app.crud.base import create_obj, get_obj_by_field

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def register_user(db: Session, user_in: UserCreate) -> User:
    existing_user = get_obj_by_field(db, User, "login", user_in.login)
    if existing_user:
        raise ValueError("User already exists")

    user = User(login=user_in.login, password=hash_password(user_in.password), status_id=1)
    return create_obj(db, user)


def authenticate_user(db: Session, login: str, password: str) -> User | None:
    user = get_obj_by_field(db, User, "login", login)
    if not user or not verify_password(password, user.password):
        return None
    return user
