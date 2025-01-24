from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.repositories.building.building import BuildingRepository
from src.repositories.organizations.organizations import OrganizationRepository
from src.entities.organizations import OrganizationsInBuildingSchema


class OrganizationsInBuildingUseCase:
    def __init__(
            self,
            organization_repo: OrganizationRepository = Depends(),
    ):
        self.organization_repo = organization_repo

    async def all_organizations_in_building(
            self,
            address: str,
    ) -> list[OrganizationsInBuildingSchema]:
        result = await self.organization_repo.get_organizations_in_building(address=address)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
