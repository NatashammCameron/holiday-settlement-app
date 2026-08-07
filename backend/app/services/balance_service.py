from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.models.participant import Participant


def calculate_balances(
    holiday_id: int,
    db: Session
):
    participants = (
        db.query(Participant)
        .filter(
            Participant.holiday_id == holiday_id
        )
        .all()
    )

    balances = {}

    for participant in participants:
        balances[participant.name] = 0

    expenses = (
        db.query(Expense)
        .filter(
            Expense.holiday_id == holiday_id
        )
        .all()
    )

    for expense in expenses:

        payer = (
            db.query(Participant)
            .filter(
                Participant.id ==
                expense.paid_by_participant_id
            )
            .first()
        )

        balances[payer.name] += float(
            expense.amount
        )

    return balances