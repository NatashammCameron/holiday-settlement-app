from pydantic import BaseModel
from pydantic import Field

class ParticipantCreate(BaseModel):
    name: str = Field(
    min_length=1,
    max_length=50)
    holiday_id: int


class ParticipantResponse(BaseModel):
    id: int
    name: str = Field(
    min_length=1,
    max_length=50)
    holiday_id: int

    class Config:
        from_attributes = True