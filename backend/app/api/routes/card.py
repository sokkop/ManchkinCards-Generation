from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.storage.postgres import get_db
from backend.app.schemas.card_types import (
    ThingCardCreate, ThingCardUpdate,
    BossCardCreate, BossCardUpdate,
    CurseCardCreate, CurseCardUpdate,
    OneThingCardCreate, OneThingCardUpdate,
    LevelUpCardCreate, LevelUpCardUpdate,
    ClassCardCreate, ClassCardUpdate,
    RaceCardCreate, RaceCardUpdate,
)
from backend.app.services.card_service import CardService

router = APIRouter()

def get_card_service(db: Session = Depends(get_db)) -> CardService:
    return CardService(db)

# ==== Thing Cards ====
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
    return {"detail": "Card deleted"}

# ==== Boss Cards ====
@router.post("/boss_cards/", tags=["boss_cards"])
def create_boss_card(
    card: BossCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_boss_card(card)}

@router.get("/boss_cards/{card_id}", tags=["boss_cards"])
def get_boss_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_boss_card(card_id)

@router.put("/boss_cards/{card_id}", tags=["boss_cards"])
def update_boss_card(
    card_id: int,
    card_data: BossCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_boss_card(card_id, card_data)

@router.delete("/boss_cards/{card_id}", tags=["boss_cards"])
def delete_boss_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_boss_card(card_id)
    return {"detail": "Card deleted"}

# ==== Curse Cards ====
@router.post("/curse_cards/", tags=["curse_cards"])
def create_curse_card(
    card: CurseCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_curse_card(card)}

@router.get("/curse_cards/{card_id}", tags=["curse_cards"])
def get_curse_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_curse_card(card_id)

@router.put("/curse_cards/{card_id}", tags=["curse_cards"])
def update_curse_card(
    card_id: int,
    card_data: CurseCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_curse_card(card_id, card_data)

@router.delete("/curse_cards/{card_id}", tags=["curse_cards"])
def delete_curse_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_curse_card(card_id)
    return {"detail": "Card deleted"}

# ==== One Thing Cards ====
@router.post("/one_thing_cards/", tags=["one_thing_cards"])
def create_one_thing_card(
    card: OneThingCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_one_thing_card(card)}

@router.get("/one_thing_cards/{card_id}", tags=["one_thing_cards"])
def get_one_thing_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_one_thing_card(card_id)

@router.put("/one_thing_cards/{card_id}", tags=["one_thing_cards"])
def update_one_thing_card(
    card_id: int,
    card_data: OneThingCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_one_thing_card(card_id, card_data)

@router.delete("/one_thing_cards/{card_id}", tags=["one_thing_cards"])
def delete_one_thing_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_one_thing_card(card_id)
    return {"detail": "Card deleted"}

# ==== Level Up Cards ====
@router.post("/level_up_cards/", tags=["level_up_cards"])
def create_level_up_card(
    card: LevelUpCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_level_up_card(card)}

@router.get("/level_up_cards/{card_id}", tags=["level_up_cards"])
def get_level_up_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_level_up_card(card_id)

@router.put("/level_up_cards/{card_id}", tags=["level_up_cards"])
def update_level_up_card(
    card_id: int,
    card_data: LevelUpCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_level_up_card(card_id, card_data)

@router.delete("/level_up_cards/{card_id}", tags=["level_up_cards"])
def delete_level_up_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_level_up_card(card_id)
    return {"detail": "Card deleted"}

# ==== Class Cards ====
@router.post("/class_cards/", tags=["class_cards"])
def create_class_card(
    card: ClassCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_class_card(card)}

@router.get("/class_cards/{card_id}", tags=["class_cards"])
def get_class_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_class_card(card_id)

@router.put("/class_cards/{card_id}", tags=["class_cards"])
def update_class_card(
    card_id: int,
    card_data: ClassCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_class_card(card_id, card_data)

@router.delete("/class_cards/{card_id}", tags=["class_cards"])
def delete_class_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_class_card(card_id)
    return {"detail": "Card deleted"}

# ==== Race Cards ====
@router.post("/race_cards/", tags=["race_cards"])
def create_race_card(
    card: RaceCardCreate,
    service: CardService = Depends(get_card_service),
):
    return {"id": service.create_race_card(card)}

@router.get("/race_cards/{card_id}", tags=["race_cards"])
def get_race_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    return service.get_race_card(card_id)

@router.put("/race_cards/{card_id}", tags=["race_cards"])
def update_race_card(
    card_id: int,
    card_data: RaceCardUpdate,
    service: CardService = Depends(get_card_service),
):
    return service.update_race_card(card_id, card_data)

@router.delete("/race_cards/{card_id}", tags=["race_cards"])
def delete_race_card(
    card_id: int,
    service: CardService = Depends(get_card_service),
):
    service.delete_race_card(card_id)
    return {"detail": "Card deleted"}
