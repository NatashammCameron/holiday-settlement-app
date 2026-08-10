from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

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
        .filter(
            Participant.holiday_id == holiday_id
        )
        .all()
    )

    return participants


@router.delete("/{participant_id}")
def delete_participant(
    participant_id: int,
    db: Session = Depends(get_db)
):
    participant = (
        db.query(Participant)
        .filter(
            Participant.id == participant_id
        )
        .first()
    )

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
        )

    try:
        db.delete(participant)
        db.commit()

        return {
            "message": "Participant deleted"
        }

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=(
                "Cannot delete participant "
                "because they are linked "
                "to existing expenses"
            )
        )