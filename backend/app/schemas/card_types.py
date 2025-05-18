from pydantic import BaseModel
from typing import Optional


# ===== BaseCard =====

class BaseCard(BaseModel):
    user_id: int
    public: Optional[bool] = True
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    like_count: Optional[int] = 0

    class Config:
        from_attributes = True


# ===== ThingCards =====

class ThingCardBase(BaseCard):
    bonus_count: Optional[int] = None
    is_big: Optional[bool] = None
    arm_count: Optional[int] = None
    cost: Optional[int] = None

class ThingCardCreate(ThingCardBase):
    pass

class ThingCardUpdate(ThingCardBase):
    pass

class ThingCardOut(ThingCardBase):
    id: int


# ===== BossCards =====

class BossCardBase(BaseCard):
    level: int
    obscenity: Optional[str] = None
    level_up_count: Optional[int] = None
    treasure_count: Optional[int] = None

class BossCardCreate(BossCardBase):
    pass

class BossCardUpdate(BaseCard):
    level: Optional[int]
    obscenity: Optional[str]
    level_up_count: Optional[int]
    treasure_count: Optional[int]

class BossCardOut(BossCardBase):
    id: int


# ===== CurseCards =====

class CurseCardBase(BaseCard):
    curse_text: str

class CurseCardCreate(CurseCardBase):
    pass

class CurseCardUpdate(BaseCard):
    curse_text: Optional[str]

class CurseCardOut(CurseCardBase):
    id: int


# ===== OneThingCards =====

class OneThingCardBase(BaseCard):
    features: Optional[str]
    cost: Optional[int]

class OneThingCardCreate(OneThingCardBase):
    pass

class OneThingCardUpdate(OneThingCardBase):
    pass

class OneThingCardOut(OneThingCardBase):
    id: int


# ===== LevelUpCards =====

class LevelUpCardBase(BaseCard):
    level: Optional[int] = 1

class LevelUpCardCreate(LevelUpCardBase):
    pass

class LevelUpCardUpdate(BaseCard):
    level: Optional[int]

class LevelUpCardOut(LevelUpCardBase):
    id: int


# ===== ClassCards =====

class ClassCardBase(BaseCard):
    features: Optional[str]

class ClassCardCreate(ClassCardBase):
    pass

class ClassCardUpdate(BaseCard):
    features: Optional[str]

class ClassCardOut(ClassCardBase):
    id: int


# ===== RaceCards =====

class RaceCardBase(BaseCard):
    features: Optional[str]

class RaceCardCreate(RaceCardBase):
    pass

class RaceCardUpdate(BaseCard):
    features: Optional[str]

class RaceCardOut(RaceCardBase):
    id: int


# ===== UpdateCards =====

class UpdateCardBase(BaseCard):
    card_id: int
    treasure_count: Optional[int] = 0

class UpdateCardCreate(UpdateCardBase):
    pass

class UpdateCardUpdate(BaseCard):
    card_id: Optional[int]
    treasure_count: Optional[int]

class UpdateCardOut(UpdateCardBase):
    id: int
