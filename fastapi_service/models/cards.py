from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, Date, Text, JSON,
    UniqueConstraint
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey("user_status.id"), nullable=False)

    collections = relationship("Collection", back_populates="creator")


class UserStatus(Base):
    __tablename__ = "user_status"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_open = Column(Boolean, default=True)

    creator = relationship("User", back_populates="collections")


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey("card_types.id"), nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_open = Column(Boolean, default=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    image = Column(String, nullable=True)

    attributes = Column(JSON, nullable=True)  # Динамические атрибуты карты

    creator = relationship("User")
    type = relationship("CardType")


class CardType(Base):
    __tablename__ = "card_types"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class CardCollection(Base):
    """Объединяет карты и коллекции + флаг избранного"""
    __tablename__ = "card_collections"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    collection_id = Column(Integer, ForeignKey("collections.id"),
                           nullable=False)
    is_favourite = Column(Boolean, default=False)

    __table_args__ = (UniqueConstraint("card_id", "collection_id"),)


class Likes(Base):
    """Общая таблица для лайков карт и коллекций"""
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_id = Column(Integer, nullable=False)  # ID лайкнутой сущности
    target_type = Column(String, nullable=False)  # "card" или "collection"

    __table_args__ = (UniqueConstraint("user_id", "target_id", "target_type"),)


class CardComment(Base):
    __tablename__ = "card_comments"

    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)


class CollectionComment(Base):
    __tablename__ = "collection_comments"

    id = Column(Integer, primary_key=True)
    collection_id = Column(Integer, ForeignKey("collections.id"),
                           nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    is_changed = Column(Boolean, default=False)
