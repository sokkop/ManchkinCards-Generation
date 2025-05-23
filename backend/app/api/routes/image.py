from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter, Depends
from fastapi.responses import FileResponse
import os
import shutil
from uuid import uuid4

from backend.app.services.image_service import apply_munchkin_style

from backend.app.api.routes.auth import security

router = APIRouter(tags=["image"])
#dependencies=[Depends(security.access_token_required)]
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # backend/app/
print(BASE_DIR)
ORIGINALS_DIR = BASE_DIR / "images" / "originals"
STYLED_DIR = BASE_DIR / "images" / "styled"

ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)
STYLED_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/style/")
async def style_image(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=400, detail="Поддерживаются только jpg/jpeg/png файлы.")

    # Сохраняем оригинал
    extension = os.path.splitext(file.filename)[-1]
    unique_name = f"{uuid4().hex}{extension}"
    original_path = os.path.join(ORIGINALS_DIR, unique_name)

    print(original_path)



    with open(original_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        print(f"Сохранён оригинал: {os.path.exists(original_path)} — {original_path}")

    print(f"Имя файла: {file.filename}")
    print(f"Сохранён как: {original_path}")

    try:
        # Обработка изображения
        styled_path = os.path.join(STYLED_DIR, f"munchkin_{unique_name}")
        apply_munchkin_style(original_path, styled_image_path=styled_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обработке изображения: {e}")

    return {
        "original_url": f"/images/originals/{unique_name}",
        "styled_url": f"/images/styled/munchkin_{unique_name}"
    }

# Роуты для отдачи изображений
@router.get("/images/originals/{filename}")
def get_original(filename: str):
    path = os.path.join(ORIGINALS_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Файл не найден")
    return FileResponse(path, media_type="image/jpeg")

@router.get("/images/styled/{filename}")
def get_styled(filename: str):
    path = os.path.join(STYLED_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Файл не найден")
    return FileResponse(path, media_type="image/jpeg")
