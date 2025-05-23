from sqlalchemy.orm import Session

# Добавление нового пользователя
def create_user(db: Session, user: schemas.UserLogin) -> models.User:
    hashed_password = auth.hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Получение пользователя по имени
def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()
