from sqlalchemy import String, Integer
from geoalchemy2 import Geometry
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base
from src.models.organization.organization import Organization


class Building(Base):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(
        Geometry(geometry_type="POINT", srid=4326),
        nullable=False,
    )
    #
    # organization: Mapped[list['Organization']] = relationship(
    #     "Organization",
    #     back_populates="building"
    # )
