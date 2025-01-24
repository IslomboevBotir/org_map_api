
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


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
