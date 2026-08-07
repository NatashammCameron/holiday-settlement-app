from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.balance_service import (
    calculate_balances
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