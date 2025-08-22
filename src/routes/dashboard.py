from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from Trawell.config.db import db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "Templates"))


router=APIRouter()

def get_loggedin_user(request: Request):
    token = request.cookies.get('user_session')
    result = db.auth.get_user(token)
    if hasattr(result, 'user'):
         return result.user
    return None

@router.get('/dashboard')
def dashboard(request: Request):
    try:
        user = get_loggedin_user(request)
        if user:
            return Templates.TemplateResponse('dashboard.html', { 'request': request})
        return RedirectResponse('/login', status_code=302)
    except Exception as e:
        return str(e)