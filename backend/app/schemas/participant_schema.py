from pydantic import BaseModel


class ParticipantCreate(BaseModel):
    name: str
    holiday_id: int


class ParticipantResponse(BaseModel):
    id: int
    name: str
    holiday_id: int

    class Config:
        from_attributes = True