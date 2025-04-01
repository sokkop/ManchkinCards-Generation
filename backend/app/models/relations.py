from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CardCollection(Base):
    __tablename__ = "card_collection"

    id = Column(Integer, primary_key=True, index=True)
    collection_id = Column(Integer, ForeignKey("collection.id"), nullable=False)
    card_id = Column(Integer, ForeignKey("card.id"), nullable=False)

    collection = relationship("Collection")
    card = relationship("Card")