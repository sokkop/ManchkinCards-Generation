from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.storage.postgres import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    status_id = Column(Integer, nullable=False)
