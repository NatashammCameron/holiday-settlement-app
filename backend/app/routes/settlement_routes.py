from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.balance_service import (
    calculate_balances
)
from app.services.settlement_service import (
    calculate_net_balances
)

router = APIRouter(
    prefix="/settlements",
    tags=["Settlements"]
)


@router.get(
    "/{holiday_id}/balances"
)
def get_balances(
    holiday_id: int,
    db: Session = Depends(get_db)
):
    return calculate_balances(
        holiday_id,
        db
    )



from app.database.dependencies import get_db
from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit

router = APIRouter(
    prefix="/settlements",
    tags=["Settlements"]
)
@router.get(
    "/expense/{expense_id}"
)
def get_expense_share(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    splits = (
        db.query(ExpenseSplit)
        .filter(
            ExpenseSplit.expense_id == expense_id
        )
        .all()
    )

    share = (
        float(expense.amount)
        / len(splits)
    )

    return {
        "expense_id": expense_id,
        "share_per_person": share,
        "participants": len(splits)
    }

@router.get(
    "/holiday/{holiday_id}/balances"
)
def holiday_balances(
    holiday_id: int,
    db: Session = Depends(get_db)
):
    return calculate_net_balances(
        holiday_id,
        db
    )