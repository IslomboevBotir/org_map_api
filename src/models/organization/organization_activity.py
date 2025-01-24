from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base

if TYPE_CHECKING:
    from src.models.organization.organization import Organization
    from src.models.activities.activity import Activity


class OrganizationActivity(Base):
    __tablename__ = "organization_activity"

    organization_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("organization.id"),
        primary_key=True
    )
    activity_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("activity.id"),
        primary_key=True
    )

    # organization: Mapped["Organization"] = relationship(
    #     "Organization",
    #     back_populates="organization_activity"
    # )
    # activity: Mapped["Activity"] = relationship(
    #     "Activity",
    #     back_populates="organization_activity"
    # )
