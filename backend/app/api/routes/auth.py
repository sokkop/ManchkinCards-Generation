from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from authx import AuthX, AuthXConfig

from backend.app.core.storage.postgres import get_db, settings
from backend.app.schemas.user import UserCreate, UserOut
from backend.app.services.auth_service import register_user, authenticate_user

router = APIRouter(tags=["auth"])

config = AuthXConfig()
config.JWT_SECRET_KEY = settings.jwt_secret_key
config.JWT_ACCESS_COOKIE_NAME = settings.jwt_access_cookie_name
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False


security = AuthX(config=config)

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(db, user_in)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(username: str, password: str, response: Response, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Bad credentials")

    token = security.create_access_token(uid=user.login)
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
    return {"access_token": token}

@router.get("/me", dependencies=[Depends(security.access_token_required)])
def get_me():
    return {"message": "Welcome to your account"}
