from http import HTTPStatus

from fastapi import Depends, HTTPException

from src.repositories.organizations.organizations import OrganizationRepository


class OrganizationsInActivityUseCase:
    def __init__(
            self,
            organization_repository: OrganizationRepository = Depends(),
    ):
        self.organization_repository = organization_repository

    async def organizations_in_activity(
            self,
            activity_name: str,
    ):
        result = await self.organization_repository.get_organizations_in_activity(activity=activity_name)
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
            )
        return result
