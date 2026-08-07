from pydantic import BaseModel


class HolidayCreate(BaseModel):
    name: str


class HolidayResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True