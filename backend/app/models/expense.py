from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(
        Integer,
        primary_key=True
    )

    description = Column(
        String,
        nullable=False
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    holiday_id = Column(
    Integer,
    ForeignKey(
        "holidays.id",
        ondelete="CASCADE"
    ),
    nullable=False
)

    paid_by_participant_id = Column(
    Integer,
    ForeignKey(
        "participants.id",
        ondelete="CASCADE"
    ),
    nullable=False
)

    holiday = relationship(
        "Holiday",
        back_populates="expenses"
    )

    splits = relationship(
        "ExpenseSplit",
        cascade="all, delete-orphan"
    )