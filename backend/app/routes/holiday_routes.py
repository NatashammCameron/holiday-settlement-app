from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.holiday import Holiday
from app.schemas.holiday_schema import (
    HolidayCreate,
    HolidayResponse
)

router = APIRouter(
    prefix="/holidays",
    tags=["Holidays"]
)


@router.post(
    "/",
    response_model=HolidayResponse
)
def create_holiday(
    holiday: HolidayCreate,
    db: Session = Depends(get_db)
):
    new_holiday = Holiday(
        name=holiday.name
    )

    db.add(new_holiday)
    db.commit()
    db.refresh(new_holiday)

    return new_holiday