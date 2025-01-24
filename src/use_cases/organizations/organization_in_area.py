from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.entities.organizations import OrganizationInAreaQueryParamsSchema, OrganizationSchema
from src.repositories.organizations.organizations import OrganizationRepository


class OrganizationInAreaUseCase:
    def __init__(
            self,
            repository: OrganizationRepository = Depends(),
    ):
        self._repository = repository

    async def get_organization_in_area(
            self,
            coordinates: OrganizationInAreaQueryParamsSchema
    ) -> list[OrganizationSchema]:
        result = await self._repository.get_organizations_in_area(coordinates=coordinates)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
