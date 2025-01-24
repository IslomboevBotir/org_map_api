from fastapi import APIRouter, Depends, status, Query

from src.use_cases.organizations.organizations_in_building import OrganizationsInBuildingUseCase
from src.entities.organizations import OrganizationsInBuildingSchema, OrganizationsActivitySchema
from src.use_cases.organizations.organizations_in_activity import OrganizationsInActivityUseCase

router = APIRouter()


@router.get(
    "/in-building",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationsInBuildingSchema],
)
async def all_organizations_in_building(
        building_address: str = Query(..., alias="building_address"),
        use_case: OrganizationsInBuildingUseCase = Depends(),
):
    return await use_case.all_organizations_in_building(address=building_address)


@router.get(
    "/activity",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationsActivitySchema],
)
async def all_organizations_in_activities(
        activity_name: str = Query(..., alias="activity_name"),
        use_case: OrganizationsInActivityUseCase = Depends(),
):
    return await use_case.organizations_in_activity(activity_name=activity_name)
