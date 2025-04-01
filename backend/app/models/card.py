from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    type_id = Column(Integer, ForeignKey("card_type.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_open = Column(Boolean, default=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)
    like_count = Column(Integer, default=0)

    card_type = relationship("CardType")


class CardLike(Base):
    __tablename__ = "card_likes"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class CardComment(Base):
    __tablename__ = "card_comments"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)


class FavouritesCard(Base):
    __tablename__ = "favourites_cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
