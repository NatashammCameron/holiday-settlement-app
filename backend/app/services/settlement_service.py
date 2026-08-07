from collections import defaultdict

from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit
from app.models.participant import Participant
def calculate_net_balances(
    holiday_id,
    db
):
    balances = defaultdict(float)

    participants = (
        db.query(Participant)
        .filter(
            Participant.holiday_id == holiday_id
        )
        .all()
    )

    for participant in participants:
        balances[participant.id] = 0

    expenses = (
        db.query(Expense)
        .filter(
            Expense.holiday_id == holiday_id
        )
        .all()
    )

    for expense in expenses:

        splits = (
            db.query(ExpenseSplit)
            .filter(
                ExpenseSplit.expense_id == expense.id
            )
            .all()
        )

        share_amount = (
            float(expense.amount)
            / len(splits)
        )

        balances[
            expense.paid_by_participant_id
        ] += float(expense.amount)

        for split in splits:
            balances[
                split.participant_id
            ] -= share_amount

    return balances