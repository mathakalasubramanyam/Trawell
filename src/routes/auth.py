from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from Trawell.config.db import db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "Templates"))


router=APIRouter()

@router.get("/login")
def login(request: Request):
    return Templates.TemplateResponse('login.html', {"request": request})

@router.post('/login')
def login_user(request: Request, email = Form(...), password = Form(...)):
    result = db.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    if result.user:
       response =  RedirectResponse('/dashboard', status_code=302)
       response.set_cookie('user_session', result.session.access_token, max_age=3600)
       return response
    





