from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.app.models import *
from backend.app.schemas.user import UserCreate
from passlib.context import CryptContext
from backend.app.crud.base import *

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_user(db: Session, user: UserCreate):
    try:
        existing_user = get_obj_by_field(db, User, 'login', user.login)
        if existing_user:
            raise HTTPException(status_code=400, detail="login already taken")

        hashed_password = pwd_context.hash(user.password)

        db_user = create_obj(db, User(
            login=user.login,
            password=hashed_password,
            status_id=1,
        ))

        return db_user.id

    except HTTPException as e:
        raise e

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")