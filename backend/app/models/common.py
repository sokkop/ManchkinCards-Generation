from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from backend.app.core.storage.postgres import Base

class CardCollections(Base):
    """Объединяет карты и коллекции"""
    __tablename__ = "card_collections"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"),
                           nullable=False)






