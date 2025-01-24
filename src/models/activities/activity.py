from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    parent_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("activity.id"),
        nullable=True
    )

    # parent: Mapped["Activity"] = relationship(
    #     "Activity",
    #     remote_side="Activity.id",
    #     backref="children"
    # )
