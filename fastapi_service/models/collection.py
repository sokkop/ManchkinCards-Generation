from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_service.storage.postgres import Base


class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="collections")
    comments = relationship("Comment", back_populates="collection")
