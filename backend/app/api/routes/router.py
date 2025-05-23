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


@router.get("/createracecard")
async def get_create_race_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_race.html', context={'request': request})


@router.get("/createclasscard")
async def get_create_class_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_class.html', context={'request': request})


@router.get("/createcursecard")
async def get_create_curse_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_curse.html', context={'request': request})


@router.get("/createlevelupcard")
async def get_create_level_up_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_level_up.html', context={'request': request})


@router.get("/createmonstercard")
async def get_create_monster_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_monster.html', context={'request': request})


@router.get("/createmodifiercard")
async def get_create_modifier_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_modifier.html', context={'request': request})


@router.get("/createthingcard")
async def get_create_thing_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_thing.html', context={'request': request})


@router.get("/createonethingcard")
async def get_create_one_thing_card_html(request: Request):
    return templates.TemplateResponse(name='CreatePages/create_one_thing.html', context={'request': request})
