from fastapi import FastAPI
from app.api.routes.home import router as home_router
from app.core.config import settings
from app.api.routes.auth import router as auth_router


app = FastAPI (title = settings.app_name,version = settings.app_version,)


app.include_router(home_router)
app.include_router(auth_router)