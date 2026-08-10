from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(Integer, primary_key=True)

    name = Column(
        String,
        nullable=False
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