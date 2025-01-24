from fastapi import APIRouter, status, Query, Depends

from src.use_cases.activity.organizations_by_activity import OrganizationsByActivityUseCase
from src.entities.activity import OrganizationByActivitySchema

router = APIRouter()


@router.get(
    "/organizations",
    status_code=status.HTTP_200_OK,
    response_model=list[OrganizationByActivitySchema]
)
async def organizations_by_activity(
        activity_name: str = Query(..., alias="activity_name"),
        use_case: OrganizationsByActivityUseCase = Depends()
):
    return await use_case.get_organizations_by_activity(name=activity_name)
