from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey("user_status.id"), nullable=False)

    collections = relationship("Collection", back_populates="creator")


class UserStatus(Base):
    __tablename__ = "user_status"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
