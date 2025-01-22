from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.organization.organization import Organization
from src.models.activities.activity import Activity


class OrganizationActivity(Base):
    __tablename__ = 'organization_activity'

    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'), primary_key=True)
    activity_id: Mapped[int] = mapped_column(ForeignKey('activity.id'), primary_key=True)

    organization: Mapped['Organization'] = relationship(back_populates='activities')
    activity: Mapped['Activity'] = relationship(back_populates='organizations')
