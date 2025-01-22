from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.organization.organization import Organization


class PhoneNumber(Base):
    __tablename__ = 'phone_number'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String, nullable=False)
    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))

    organization: Mapped['Organization'] = relationship(back_populates='phone_numbers')
