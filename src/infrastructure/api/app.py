from fastapi import FastAPI

from src.interfaces.api.organizations.router import router as organizations_router


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(organizations_router, prefix="/organizations")
    return _app
