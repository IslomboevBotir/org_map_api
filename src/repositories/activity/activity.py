from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.entities.activity import OrganizationByActivitySchema
from src.infrastructure.db.config import async_general_session
from src.serializers.activity import OrganizationByActivitySerializer
from src.models import Activity, Organization, OrganizationActivity


class ActivityRepository:
    def __init__(
            self,
            session: AsyncSession = Depends(async_general_session),
            serialize_organization_by_activity: OrganizationByActivitySerializer = Depends()
    ):
        self.session = session
        self.serialize = serialize_organization_by_activity

    async def get_organizations_by_activity(
            self,
            name: str
    ) -> list[OrganizationByActivitySchema]:
        activity_tree = (
            select(Activity.id, Activity.name, Activity.parent_id)
            .where(Activity.name == name)
            .cte(name="activity_tree", recursive=True)
        )

        activity_tree = activity_tree.union_all(
            select(Activity.id, Activity.name, Activity.parent_id)
            .join(activity_tree, Activity.parent_id == activity_tree.c.id)
        )

        stmt = (
            select(Organization.id.label("organization_id"), Organization.name.label("organization_name"))
            .join(OrganizationActivity, Organization.id == OrganizationActivity.organization_id)
            .join(activity_tree, OrganizationActivity.activity_id == activity_tree.c.id)
        )
        try:
            res = await self.session.execute(stmt)
            mapped_res = res.mappings().all()
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=str(e),
            )

        return self.serialize.serializer_list(mapped_res)
