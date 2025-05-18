from fastapi import FastAPI
from backend.app.api.routes.router import router as router_pages
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='static'), 'static')