from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


if TYPE_CHECKING:
    from src.models.building.building import Building
    from src.models.organization.organization_phones import OrganizationPhone
    from src.models.organization.organization_activity import OrganizationActivity


class Organization(Base):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    building_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("building.id"),
        nullable=False
    )

    # building: Mapped["Building"] = relationship(
    #     "Building",
    #     back_populates="organization"
    # )
    # phones: Mapped[list["OrganizationPhone"]] = relationship(
    #     "OrganizationPhone",
    #     back_populates="organization"
    # )
    # activity: Mapped[list["OrganizationActivity"]] = relationship(
    #     "OrganizationActivity",
    #     back_populates="organization"
    # )
