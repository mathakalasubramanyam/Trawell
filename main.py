from fastapi import FastAPI
from Trawell.src.routes.signup import router as signup_router
from Trawell.src.routes.auth import router as auth_router
from Trawell.src.routes.dashboard import router as dash_router
app=FastAPI(title="Trawell")

app.include_router(signup_router)
app.include_router(auth_router)
app.include_router(dash_router)