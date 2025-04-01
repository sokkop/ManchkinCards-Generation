from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=["router"])
templates = Jinja2Templates(directory='frontend/templates')


@router.get("/")
async def get_main_html(request: Request):
    return templates.TemplateResponse(name='main.html', context={'request': request, 'text': "Egor popusk"})


@router.get("/login")
async def get_login_html(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})


@router.get("/auth")
async def get_auth_html(request: Request):
    return templates.TemplateResponse(name="auth.html", context={'request': request})
