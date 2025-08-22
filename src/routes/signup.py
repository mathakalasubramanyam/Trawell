from fastapi import FastAPI,APIRouter, Request

from Trawell.src.routes.auth import Templates


router=APIRouter()
@router.get("/login2")
def sign_up(request: Request):
    return Templates.TemplateResponse('signup.html', {"request": request})


