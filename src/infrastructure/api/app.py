from fastapi import FastAPI

from src.interfaces.api.organizations.router import router as organizations_router
from src.interfaces.api.activity.router import router as activity_router


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(organizations_router, prefix="/api/organizations")
    _app.include_router(activity_router, prefix="/api/activity")
    return _app
