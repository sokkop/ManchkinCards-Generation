from fastapi import FastAPI
from pages.pages import router as router_pages
import uvicorn

app = FastAPI()
app.include_router(router_pages)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8080)