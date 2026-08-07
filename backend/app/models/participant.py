from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.database import Base


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    holiday_id = Column(
        Integer,
        ForeignKey("holidays.id")
    )