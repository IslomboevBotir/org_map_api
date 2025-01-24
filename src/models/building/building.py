from sqlalchemy import String, Integer
from geoalchemy2 import Geometry
from sqlalchemy.orm import mapped_column, Mapped

from src.models.base import Base


class Building(Base):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(
        Geometry(geometry_type="POINT", srid=4326),
        nullable=False,
    )
