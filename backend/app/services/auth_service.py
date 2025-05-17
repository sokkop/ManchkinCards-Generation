# from datetime import datetime, timedelta
# import jwt
#
# from backend.app.core.config import get_settings
# from backend.app.models import *
# from backend.app.schemas.user import UserCreate
# from passlib.context import CryptContext
# from backend.app.crud.base import *
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# # Загрузить настройки из .env
# settings = get_settings()
#
# # Создание токена
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
#     return encoded_jwt
#
# # Декодирование токена
# def verify_token(token: str) -> dict:
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         return payload
#     except jwt.PyJWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#
#
# def register_user(db: Session, user: UserCreate):
#     try:
#         existing_user = get_obj_by_field(db, User, 'login', user.login)
#         if existing_user:
#             raise HTTPException(status_code=400, detail="login already taken")
#
#         hashed_password = pwd_context.hash(user.password)
#
#         db_user = create_obj(db, User(
#             login=user.login,
#             password=hashed_password,
#             status_id=1,
#         ))
#
#         return db_user.id
#
#     except HTTPException as e:
#         raise e
#
#     except SQLAlchemyError as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
#
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")