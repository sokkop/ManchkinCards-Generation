from sqlalchemy import Column, Integer, Text, ForeignKey, Boolean
from .base import Base


class ThingCard(Base):
    __tablename__ = "thing_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    bonus_count = Column(Integer)
    is_big = Column(Boolean, default=False)
    arm_count = Column(Integer)
    cost = Column(Integer)


class BossCard(Base):
    __tablename__ = "boss_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    level = Column(Integer, nullable=False)
    obscenity = Column(Text)
    level_up_count = Column(Integer)
    treasure_count = Column(Integer)


class CurseCard(Base):
    __tablename__ = "curse_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    curse_text = Column(Text)


class OneThingCard(Base):
    __tablename__ = "one_thing_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    features = Column(Text)
    cost = Column(Integer)


class LevelUpCard(Base):
    __tablename__ = "level_up_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    level = Column(Integer, default=1)


class ClassCard(Base):
    __tablename__ = "class_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    features = Column(Text)


class RaceCard(Base):
    __tablename__ = "race_cards"

    id = Column(Integer, ForeignKey("cards.id"), primary_key=True)
    features = Column(Text)


class UpdateCard(Base):
    __tablename__ = "update_cards"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    treasure_count = Column(Integer, default=0)