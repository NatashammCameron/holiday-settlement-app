from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.expense import Expense
from app.schemas.expense_schema import (
    ExpenseCreate,
    ExpenseResponse
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post(
    "/",
    response_model=ExpenseResponse
)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):
    new_expense = Expense(
        description=expense.description,
        amount=expense.amount,
        holiday_id=expense.holiday_id,
        paid_by_participant_id=expense.paid_by_participant_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense