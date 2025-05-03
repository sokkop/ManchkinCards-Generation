from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from backend.app.core.storage.postgres import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    is_open = Column(Boolean, default=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)
    like_count = Column(Integer, default=0)