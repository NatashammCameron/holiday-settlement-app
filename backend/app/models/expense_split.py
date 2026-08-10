from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from app.database.database import Base


class ExpenseSplit(Base):
    __tablename__ = "expense_splits"

    id = Column(
        Integer,
        primary_key=True
    )

    expense_id = Column(
        Integer,
        ForeignKey( "expenses.id", ondelete="CASCADE"),
        nullable=False
    )

    participant_id = Column(
        Integer,
        ForeignKey("participants.id", ondelete="CASCADE"),
        nullable=False
    )