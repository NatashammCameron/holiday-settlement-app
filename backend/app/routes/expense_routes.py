from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit
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

    for participant_id in expense.participant_ids:
        split = ExpenseSplit(
            expense_id=new_expense.id,
            participant_id=participant_id
        )

        db.add(split)

    db.commit()

    return new_expense


@router.get(
    "/",
    response_model=list[ExpenseResponse]
)
def get_expenses(
    db: Session = Depends(get_db)
):
    expenses = db.query(Expense).all()

    return expenses


@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id
        )
        .first()
    )

    if not expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    (
        db.query(ExpenseSplit)
        .filter(
            ExpenseSplit.expense_id == expense_id
        )
        .delete()
    )

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted"
    }


@router.get(
    "/holiday/{holiday_id}",
    response_model=list[ExpenseResponse]
)
def get_expenses_by_holiday(
    holiday_id: int,
    db: Session = Depends(get_db)
):
    expenses = (
        db.query(Expense)
        .filter(
            Expense.holiday_id == holiday_id
        )
        .all()
    )

    return expenses