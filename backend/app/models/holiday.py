from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database.database import Base


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    user = relationship(
        "User"
    )

    participants = relationship(
        "Participant",
        back_populates="holiday",
        cascade="all, delete-orphan"
    )

    expenses = relationship(
        "Expense",
        back_populates="holiday",
        cascade="all, delete-orphan"
    )