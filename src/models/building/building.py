from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.base import Base
from src.models.organization.organization import Organization


class Building(Base):
    __tablename__ = 'building'

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)

    organizations: Mapped[list['Organization']] = relationship(
        'Organization', back_populates='building'
    )
