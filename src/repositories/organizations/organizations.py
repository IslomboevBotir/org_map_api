from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models.building.building import Building
from src.models import OrganizationActivity, Activity
from src.models.organization.organization import Organization
from src.infrastructure.db.config import async_general_session
from src.serializers.organizations import OrganizationInBuildingSerializer, OrganizationsInActivitySerializer
from src.entities.organizations import OrganizationsInBuildingSchema, OrganizationsActivitySchema


class OrganizationRepository:
    def __init__(
            self,
            serialize_organizations_in_building: OrganizationInBuildingSerializer = Depends(),
            serialize_organizations_activity: OrganizationsInActivitySerializer = Depends(),
            session: AsyncSession = Depends(async_general_session),
    ):
        self.session = session
        self.serialize_organizations_in_building = serialize_organizations_in_building
        self.serialize_organizations_activity = serialize_organizations_activity

    async def get_organizations_in_building(
            self,
            address: str,
    ) -> list[OrganizationsInBuildingSchema] | None:
        stmt = (
            select(Building.address, Organization.name)
            .select_from(Building)
            .join(Organization, Organization.building_id == Building.id, isouter=True)
            .where(Building.address == address)
        )
        res = await self.session.execute(stmt)
        mapped_res = res.mappings().all()
        return self.serialize_organizations_in_building.serializer_list(mapped_res)

    async def get_organizations_in_activity(
            self,
            activity: str,
    ) -> list[OrganizationsActivitySchema] | None:
        stmt = (
            select(Organization.name)
            .join(OrganizationActivity, Organization.id == OrganizationActivity.organization_id)
            .join(Activity, OrganizationActivity.activity_id == Activity.id)
            .where(Activity.name == activity)
        )
        result = await self.session.execute(stmt)
        mapped_res = result.mappings().all()
        return self.serialize_organizations_activity.serializer_list(mapped_res)
