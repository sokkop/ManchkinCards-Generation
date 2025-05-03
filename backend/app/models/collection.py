from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from backend.app.core.storage.postgres import Base


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    is_open = Column(Boolean, default=True)

    user = relationship("User", back_populates="collections")
