from fastapi import FastAPI
from pages.pages import router as router_pages

app = FastAPI()
app.include_router(router_pages)

@app.get("/")
def root():
    return "Egor Gasilin popusk"


@app.get("/login")
def root():
    return ""
