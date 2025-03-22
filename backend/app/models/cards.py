from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, Date, Text, JSON,
    UniqueConstraint
)
from sqlalchemy.orm import relationship, declarative_base
from backend.app.models.init import Base


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


Base = declarative_base()

# Базовая таблица для всех карт
class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)  # Указывает тип карты
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)
    is_open = Column(Boolean, default=False)
    like_count = Column(Integer, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "card",
        "polymorphic_on": type,
    }

# Наследуемая таблица для предметов
class ThingCard(Card):
    __tablename__ = "thing_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    bonus_count = Column(Integer, default=0)
    is_big = Column(Boolean, default=False)
    arm_count = Column(Integer, default=0)
    cost = Column(Integer, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "thing_card",
    }

# Наследуемая таблица для боссов
class BossCard(Card):
    __tablename__ = "boss_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    level = Column(Integer, nullable=False)
    obscenity = Column(String)
    level_up_count = Column(Integer, default=0)
    treasure_count = Column(Integer, default=0)

    __mapper_args__ = {
        "polymorphic_identity": "boss_card",
    }

# Наследуемая таблица для проклятий
class CurseCard(Card):
    __tablename__ = "curse_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    curse_text = Column(Text, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "curse_card",
    }

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
