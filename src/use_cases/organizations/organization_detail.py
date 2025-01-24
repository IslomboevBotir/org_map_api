from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.entities.organizations import OrganizationSchema
from src.repositories.organizations.organizations import OrganizationRepository


class OrganizationDetailUseCase:
    def __init__(
            self,
            repository: OrganizationRepository = Depends()
    ):
        self._repository = repository

    async def get_detail_organization_by_id(
            self,
            org_id: int
    ) -> OrganizationSchema | HTTPException:
        result = await self._repository.get_organization_by_id(org_id=org_id)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result

    async def get_detail_organization_by_name(
            self,
            org_name: str
    ) -> OrganizationSchema | HTTPException:
        result = await self._repository.get_organization_by_name(org_name=org_name)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
