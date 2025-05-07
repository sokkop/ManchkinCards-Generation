from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.storage.postgres import get_db
from backend.app.schemas.card_types import ThingCardCreate, ThingCardUpdate
from backend.app.services.card_service import CardService

router = APIRouter()

def get_card_service(db: Session = Depends(get_db)) -> CardService:
    return CardService(db)


@router.post("/thing_cards/", tags=["thing_cards"])
def create_thing_card(
    card: ThingCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_thing_card(card)}


@router.get("/thing_cards/{card_id}", tags=["thing_cards"])
def get_thing_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_thing_card(card_id)


@router.put("/thing_cards/{card_id}", tags=["thing_cards"])
def update_thing_card(
    card_id: int,
    card_data: ThingCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_thing_card(card_id, card_data)


@router.delete("/thing_cards/{card_id}", tags=["thing_cards"])
def delete_thing_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_thing_card(card_id)
    return {"detail": "Deleted"}
