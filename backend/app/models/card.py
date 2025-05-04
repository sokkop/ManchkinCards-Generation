from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Date
from backend.app.core.storage.postgres import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    public = Column(Boolean, default=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)
    like_count = Column(Integer, default=0)



class CardLikes(Base):
    __tablename__ = "cards_likes"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class CardFavorites(Base):
    __tablename__ = "card_favorites"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


class CardComments(Base):
    __tablename__ = "card_comments"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)