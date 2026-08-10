from pydantic import BaseModel
from pydantic import Field

class HolidayCreate(BaseModel):
    name: str = Field(
    min_length=1,
    max_length=100
)


class HolidayResponse(BaseModel):
    id: int
    name: str = Field(
    min_length=1,
    max_length=100
)

    class Config:
        from_attributes = True