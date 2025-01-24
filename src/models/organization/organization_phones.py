from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class OrganizationPhone(Base):
    __tablename__ = "organization_phones"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    organization_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("organization.id"),
        nullable=False
    )
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
