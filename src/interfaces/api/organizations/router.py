from fastapi import APIRouter, Depends, status, Query, Path

from src.entities.organizations import OrganizationsInBuildingSchema, OrganizationsActivitySchema, OrganizationSchema
from src.use_cases.organizations.organizations_in_building import OrganizationsInBuildingUseCase
from src.use_cases.organizations.organizations_in_activity import OrganizationsInActivityUseCase
from src.use_cases.organizations.organization_detail import OrganizationDetailUseCase

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


@router.get(
    "/detail/{organization_id}/",
    status_code=status.HTTP_200_OK,
    response_model=OrganizationSchema
)
async def organization_detail_by_id(
        organization_id: int = Path(..., alias="organization_id"),
        use_case: OrganizationDetailUseCase = Depends()
):
    return await use_case.get_detail_organization_by_id(org_id=organization_id)


@router.get(
    "/detail",
    status_code=status.HTTP_200_OK,
    response_model=OrganizationSchema
)
async def organization_detail_by_name(
        organization_name: str = Query(..., alias="organization_name"),
        use_case: OrganizationDetailUseCase = Depends(),
):
    return await use_case.get_detail_organization_by_name(org_name=organization_name)
