from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Holiday(Base):
    __tablename__ = "holidays"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)