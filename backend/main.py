import os

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.app.api.main import api_router
import uvicorn

from backend.app.core.config import get_settings
from backend.app.core.storage.postgres import Base, engine

app = FastAPI()
app.include_router(api_router)

Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../static")),
    name="static"
)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8080)
