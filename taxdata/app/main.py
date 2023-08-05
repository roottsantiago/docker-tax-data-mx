"""
Script manages the app
"""
from fastapi import FastAPI
from taxdata.app.router import api_router

from taxdata.app.core.config import settings

app = FastAPI(
    title=settings.PROYECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)


app.include_router(api_router, prefix=settings.API_STR)
