from decimal import Decimal

from pydantic import BaseModel
from pydantic import Field

class ExpenseCreate(BaseModel):
    description: str
    amount: Decimal = Field(gt=0)
    holiday_id: int
    paid_by_participant_id: int
    participant_ids: list[int]


class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: Decimal = Field(gt=0)
    holiday_id: int
    paid_by_participant_id: int

    class Config:
        from_attributes = True