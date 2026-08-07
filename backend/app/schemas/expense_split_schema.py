from pydantic import BaseModel


class ExpenseSplitCreate(BaseModel):
    expense_id: int
    participant_id: int