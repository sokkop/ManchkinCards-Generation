import os
from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.app.api.main import api_router
import uvicorn

from authx.exceptions import MissingTokenError
from fastapi.responses import JSONResponse
from fastapi import Request
from backend.app.core.storage.postgres import Base, engine

app = FastAPI()
app.include_router(api_router)

@app.exception_handler(MissingTokenError)
async def missing_token_handler(request: Request, exc: MissingTokenError):
    return JSONResponse(
        status_code=403,
        content={"detail": "Access token is missing. Please log in."}
    )

Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent
app.mount("/images", StaticFiles(directory=BASE_DIR / "images"), name="images")

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../static")),
    name="static"
)

app.mount("/images", StaticFiles(directory=BASE_DIR / "images"), name="images")

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8080)
