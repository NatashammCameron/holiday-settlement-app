from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.participant import Participant
from app.schemas.participant_schema import (
    ParticipantCreate,
    ParticipantResponse
)

router = APIRouter(
    prefix="/participants",
    tags=["Participants"]
)


@router.post(
    "/",
    response_model=ParticipantResponse
)
def create_participant(
    participant: ParticipantCreate,
    db: Session = Depends(get_db)
):
    new_participant = Participant(
        name=participant.name,
        holiday_id=participant.holiday_id
    )

    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)

    return new_participant

@router.get(
    "/",
    response_model=list[ParticipantResponse]
)
def get_participants(
    db: Session = Depends(get_db)
):
    participants = db.query(Participant).all()

    return participants

@router.get(
    "/holiday/{holiday_id}",
    response_model=list[ParticipantResponse]
)
def get_participants_by_holiday(
    holiday_id: int,
    db: Session = Depends(get_db)
):
    participants = (
        db.query(Participant)
        .filter(Participant.holiday_id == holiday_id)
        .all()
    )

    return participants