from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/")
async def get_main_html(request: Request):
    return templates.TemplateResponse(name='main.html', context={'request': request, 'text': "Sonya popusk"})


@router.get("/login")
async def get_login_html(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})
