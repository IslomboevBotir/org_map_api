from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models.building.building import Building
from src.models.organization.organization import Organization
from src.infrastructure.db.config import async_general_session


class BuildingRepository:
    def __init__(
            self,
            session: AsyncSession = Depends(async_general_session)
    ):
        self.session = session
