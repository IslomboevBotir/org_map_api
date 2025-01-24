from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.repositories.organizations.organizations import OrganizationRepository
from src.entities.organizations import OrganizationNearbyQueryParamsSchema, OrganizationSchema


class OrganizationNearbyUseCase:
    def __init__(
            self,
            repository: OrganizationRepository = Depends()
    ):
        self.repository = repository

    async def get_organization_nearby(
            self,
            location: OrganizationNearbyQueryParamsSchema
    ) -> list[OrganizationSchema]:
        result = await self.repository.get_organization_nearby(location=location)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
