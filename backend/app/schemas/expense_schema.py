from decimal import Decimal

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    description: str
    amount: Decimal
    holiday_id: int
    paid_by_participant_id: int


class ExpenseResponse(BaseModel):
    id: int
    description: str
    amount: Decimal
    holiday_id: int
    paid_by_participant_id: int

    class Config:
        from_attributes = True