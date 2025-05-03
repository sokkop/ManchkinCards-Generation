from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, String, Boolean
from sqlalchemy.orm import relationship
from backend.app.core.storage.postgres import Base



class Likes(Base):
    """Общая таблица для лайков карт и коллекций"""
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    target_id = Column(Integer, nullable=False)  # ID лайкнутой сущности
    target_type = Column(String, nullable=False)  # "card" или "collection"

    __table_args__ = (UniqueConstraint("user_id", "target_id", "target_type"),)



class CardCollection(Base):
    """Объединяет карты и коллекции + флаг избранного"""
    __tablename__ = "card_collections"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("card.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"),
                           nullable=False)
    is_favourite = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("card_id", "collection_id"),)



class FavouritesCollection(Base):
    __tablename__ = "favourites_collections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False)


class CardLike(Base):
    __tablename__ = "card_likes"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)


class CardComment(Base):
    __tablename__ = "card_comments"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)
