from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.holiday import Holiday
from app.models.user import User

from app.auth.dependencies import (
    get_current_user
)

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
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    new_holiday = Holiday(
        name=holiday.name,
        user_id=current_user.id
    )

    db.add(new_holiday)
    db.commit()
    db.refresh(new_holiday)

    return new_holiday


@router.get(
    "/",
    response_model=list[HolidayResponse]
)
def get_holidays(
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    holidays = (
        db.query(Holiday)
        .filter(
            Holiday.user_id == current_user.id
        )
        .all()
    )

    return holidays


@router.put(
    "/{holiday_id}",
    response_model=HolidayResponse
)
def update_holiday(
    holiday_id: int,
    holiday: HolidayCreate,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    existing_holiday = (
        db.query(Holiday)
        .filter(
            Holiday.id == holiday_id,
            Holiday.user_id == current_user.id
        )
        .first()
    )

    if not existing_holiday:
        raise HTTPException(
            status_code=404,
            detail="Holiday not found"
        )

    existing_holiday.name = holiday.name

    db.commit()
    db.refresh(existing_holiday)

    return existing_holiday


@router.get(
    "/{holiday_id}",
    response_model=HolidayResponse
)
def get_holiday(
    holiday_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    holiday = (
        db.query(Holiday)
        .filter(
            Holiday.id == holiday_id,
            Holiday.user_id == current_user.id
        )
        .first()
    )

    if not holiday:
        raise HTTPException(
            status_code=404,
            detail="Holiday not found"
        )

    return holiday


@router.delete(
    "/{holiday_id}"
)
def delete_holiday(
    holiday_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    holiday = (
        db.query(Holiday)
        .filter(
            Holiday.id == holiday_id,
            Holiday.user_id == current_user.id
        )
        .first()
    )

    if not holiday:
        raise HTTPException(
            status_code=404,
            detail="Holiday not found"
        )

    db.delete(holiday)
    db.commit()

    return {
        "message": "Holiday deleted"
    }