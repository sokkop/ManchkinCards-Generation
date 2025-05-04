from sqlalchemy.orm import Session
from fastapi import HTTPException
from backend.app.models import ThingCards, Card
from backend.app.schemas.card_types import ThingCardCreate, ThingCardUpdate
from backend.app.crud.base import create_obj, update_obj, delete_obj, get_obj_by_id


class CardService:
    def __init__(self, db: Session):
        self.db = db

    def create_thing_card(self, card_data: ThingCardCreate) -> int:
        base_card_data = Card(
            user_id=card_data.user_id,
            public=card_data.public,
            name=card_data.name,
            description=card_data.description,
            image=card_data.image,
            like_count=card_data.like_count
        )

        base_card = create_obj(self.db, base_card_data)

        card = ThingCards(
            id=base_card.id,
            bonus_count=card_data.bonus_count,
            is_big=card_data.is_big,
            arm_count=card_data.arm_count,
            cost=card_data.cost
        )

        created_card = create_obj(self.db, card)
        return created_card.id

    def get_thing_card(self, card_id: int) -> ThingCards:
        card = get_obj_by_id(self.db, ThingCards, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

    def update_thing_card(self, card_id: int, update_data: ThingCardUpdate) -> ThingCards:
        updates = update_data.model_dump(exclude_unset=True)
        updated_card = update_obj(self.db, ThingCards, card_id, updates)
        if not updated_card:
            raise HTTPException(status_code=404, detail="Card not found")
        return updated_card

    def delete_thing_card(self, card_id: int):
        delete_obj(self.db, ThingCards, card_id)


