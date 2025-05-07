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


@router.get("/create")
async def get_create_card_change_hrml(request: Request):
    return templates.TemplateResponse(name="create_card_change.html", context={'request': request})


@router.get("/profile")
async def get_profile_html(request: Request):
    return templates.TemplateResponse(name="profile.html", context={'request': request})


@router.get("/cardinformation")
async def get_card_comment_html(request: Request):
    return templates.TemplateResponse(name='card_information.html', context={'request': request})
