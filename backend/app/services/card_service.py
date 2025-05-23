from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.app.models import *
from backend.app.schemas.card_types import *
from backend.app.crud.base import create_obj, update_obj, delete_obj, get_obj_by_id


class CardService:
    def __init__(self, db: Session):
        self.db = db

    # ==== ThingCards ====
    def create_thing_card(self, card_data: ThingCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = ThingCards(
            id=base_card.id,
            bonus_count=card_data.bonus_count,
            is_big=card_data.is_big,
            arm_count=card_data.arm_count,
            cost=card_data.cost
        )
        return create_obj(self.db, card).id

    def get_thing_card(self, card_id: int) -> ThingCards:
        card = get_obj_by_id(self.db, ThingCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_thing_card(self, card_id: int, update_data: ThingCardUpdate) -> ThingCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, ThingCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_thing_card(self, card_id: int):
        delete_obj(self.db, ThingCards, card_id)

    # ==== BossCards ====
    def create_boss_card(self, card_data: BossCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = BossCards(
            id=base_card.id,
            level=card_data.level,
            obscenity=card_data.obscenity,
            level_up_count=card_data.level_up_count,
            treasure_count=card_data.treasure_count
        )
        return create_obj(self.db, card).id

    def get_boss_card(self, card_id: int) -> BossCards:
        card = get_obj_by_id(self.db, BossCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_boss_card(self, card_id: int, update_data: BossCardUpdate) -> BossCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, BossCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_boss_card(self, card_id: int):
        delete_obj(self.db, BossCards, card_id)

    # ==== CurseCards ====
    def create_curse_card(self, card_data: CurseCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = CurseCards(
            id=base_card.id,
            curse_text=card_data.curse_text
        )
        return create_obj(self.db, card).id

    def get_curse_card(self, card_id: int) -> CurseCards:
        card = get_obj_by_id(self.db, CurseCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_curse_card(self, card_id: int, update_data: CurseCardUpdate) -> CurseCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, CurseCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_curse_card(self, card_id: int):
        delete_obj(self.db, CurseCards, card_id)

    # ==== OneThingCards ====
    def create_one_thing_card(self, card_data: OneThingCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = OneThingCards(
            id=base_card.id,
            features=card_data.features,
            cost=card_data.cost
        )
        return create_obj(self.db, card).id

    def get_one_thing_card(self, card_id: int) -> OneThingCards:
        card = get_obj_by_id(self.db, OneThingCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_one_thing_card(self, card_id: int, update_data: OneThingCardUpdate) -> OneThingCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, OneThingCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_one_thing_card(self, card_id: int):
        delete_obj(self.db, OneThingCards, card_id)

    # ==== LevelUpCards ====
    def create_level_up_card(self, card_data: LevelUpCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = LevelUpCards(
            id=base_card.id,
            level=card_data.level
        )
        return create_obj(self.db, card).id

    def get_level_up_card(self, card_id: int) -> LevelUpCards:
        card = get_obj_by_id(self.db, LevelUpCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_level_up_card(self, card_id: int, update_data: LevelUpCardUpdate) -> LevelUpCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, LevelUpCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_level_up_card(self, card_id: int):
        delete_obj(self.db, LevelUpCards, card_id)

    # ==== ClassCards ====
    def create_class_card(self, card_data: ClassCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = ClassCards(
            id=base_card.id,
            features=card_data.features
        )
        return create_obj(self.db, card).id

    def get_class_card(self, card_id: int) -> ClassCards:
        card = get_obj_by_id(self.db, ClassCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_class_card(self, card_id: int, update_data: ClassCardUpdate) -> ClassCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, ClassCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_class_card(self, card_id: int):
        delete_obj(self.db, ClassCards, card_id)

    # ==== RaceCards ====
    def create_race_card(self, card_data: RaceCardCreate) -> int:
        base_card = create_obj(self.db, Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        ))
        card = RaceCards(
            id=base_card.id,
            features=card_data.features
        )
        return create_obj(self.db, card).id

    def get_race_card(self, card_id: int) -> RaceCards:
        card = get_obj_by_id(self.db, RaceCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_race_card(self, card_id: int, update_data: RaceCardUpdate) -> RaceCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated = update_obj(self.db, RaceCards, card_id, updates)
        if not updated:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated

    def delete_race_card(self, card_id: int):
        delete_obj(self.db, RaceCards, card_id)



