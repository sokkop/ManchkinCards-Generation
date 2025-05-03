from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.storage.postgres import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    status_id = Column(String, nullable=False)

    collections = relationship("Collection", back_populates="user")


class UserStatus(Base):
    __tablename__ = "user_status"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
