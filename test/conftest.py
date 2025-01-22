import pytest_asyncio

from httpx import AsyncClient, ASGITransport

from src.infrastructure.api.app import create_app


@pytest_asyncio.fixture(scope='session')
async def test_client():
    app = create_app()
    async with AsyncClient(transport=ASGITransport(app=app)) as client:
        yield client
