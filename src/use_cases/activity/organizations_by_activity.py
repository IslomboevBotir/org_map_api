from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.entities.activity import OrganizationByActivitySchema
from src.repositories.activity.activity import ActivityRepository


class OrganizationsByActivityUseCase:
    def __init__(
            self,
            repository: ActivityRepository = Depends(),
    ):
        self.repository = repository

    async def get_organizations_by_activity(
            self,
            name: str
    ) -> list[OrganizationByActivitySchema]:
        result = await self.repository.get_organizations_by_activity(name=name)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
