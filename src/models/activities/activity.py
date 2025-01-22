from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.organization.organization import Organization


class Activity(Base):
    __tablename__ = 'activity'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    parent_id: Mapped[int] = mapped_column(ForeignKey('activity.id'), nullable=True)

    parent: Mapped['Activity'] = relationship(
        'Activity',
        back_populates='children',
        remote_side=[id],
        cascade='all, delete'
    )
    children: Mapped[list['Activity']] = relationship(
        'Activity',
        back_populates='parent',
        cascade='all, delete'
    )
    organizations: Mapped[list['Organization']] = relationship(
        'Organization',
        secondary='organization_activity',
        back_populates='activities'
    )
