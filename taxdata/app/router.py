"""
This script manages all the routes of the APIs.
"""
from fastapi import APIRouter

from taxdata.app.api import datafiscal

api_router = APIRouter()
api_router.include_router(datafiscal.router, prefix="/taxpayers", tags=["taxpayers"])
