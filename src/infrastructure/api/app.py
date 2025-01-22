from fastapi import FastAPI


def create_app() -> FastAPI:
    _app = FastAPI()
    return _app
