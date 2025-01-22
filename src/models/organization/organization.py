from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.building.building import Building
from src.models.organization.phone_number import PhoneNumber
from src.models.activities.activity import Activity


class Organization(Base):
    __tablename__ = 'organization'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    building_id: Mapped[int] = mapped_column(ForeignKey('building.id'))

    building: Mapped['Building'] = relationship(back_populates='organizations')
    phone_numbers: Mapped[list['PhoneNumber']] = relationship(
        'PhoneNumber',
        back_populates='organization'
    )
    activities: Mapped[list['Activity']] = relationship(
        'Activity',
        secondary='organization_activity',
        back_populates='organizations'
    )
