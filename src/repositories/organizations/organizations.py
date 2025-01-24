from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models.building.building import Building
from src.models import OrganizationActivity, Activity
from src.models.organization.organization import Organization
from src.infrastructure.db.config import async_general_session
from src.serializers.organizations import (
    OrganizationInBuildingSerializer,
    OrganizationsInActivitySerializer,
    OrganizationDetailSerializer
)
from src.entities.organizations import OrganizationsInBuildingSchema, OrganizationsActivitySchema
from src.entities.organizations import OrganizationSchema


class OrganizationRepository:
    def __init__(
            self,
            serialize_organizations_in_building: OrganizationInBuildingSerializer = Depends(),
            serialize_organizations_activity: OrganizationsInActivitySerializer = Depends(),
            serialize_organization: OrganizationDetailSerializer = Depends(),
            session: AsyncSession = Depends(async_general_session),
    ):
        self.session = session
        self.serialize_organizations_in_building = serialize_organizations_in_building
        self.serialize_organizations_activity = serialize_organizations_activity
        self.serialize_organization = serialize_organization

    async def get_organizations_in_building(
            self,
            address: str,
    ) -> list[OrganizationsInBuildingSchema]:
        try:
            stmt = (
                select(Building.address, Organization.name)
                .select_from(Building)
                .join(Organization, Organization.building_id == Building.id, isouter=True)
                .where(Building.address == address)
            )
            res = await self.session.execute(stmt)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Invalid address",
            )
        mapped_res = res.mappings().all()
        return self.serialize_organizations_in_building.serializer_list(mapped_res)

    async def get_organizations_in_activity(
            self,
            activity: str,
    ) -> list[OrganizationsActivitySchema]:
        try:
            stmt = (
                select(Organization.name)
                .join(OrganizationActivity, Organization.id == OrganizationActivity.organization_id)
                .join(Activity, OrganizationActivity.activity_id == Activity.id)
                .where(Activity.name == activity)
            )
            result = await self.session.execute(stmt)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="The provided activity does not exist",
            )

        mapped_res = result.mappings().all()
        return self.serialize_organizations_activity.serializer_list(mapped_res)

    async def get_organization_by_id(
            self,
            org_id: int
    ) -> OrganizationSchema | None:
        try:
            stmt = (
                select(Organization.name).where(Organization.id == org_id)
            )
            result = await self.session.execute(stmt)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Organization not found",
            )
        mapped_res = result.mappings().one_or_none()
        if mapped_res is None:
            return None
        return self.serialize_organization.serialize(mapped_res)

    async def get_organization_by_name(
            self,
            org_name: str
    ) -> OrganizationSchema | None:
        try:
            stmt = (
                select(Organization.name).where(Organization.name == org_name)
            )
            result = await self.session.execute(stmt)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Organization not found"
            )
        mapped_res = result.mappings().one_or_none()
        if mapped_res is None:
            return None
        return self.serialize_organization.serialize(mapped_res)
