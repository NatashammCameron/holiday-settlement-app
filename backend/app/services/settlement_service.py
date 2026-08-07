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


def calculate_settlements(
    balances,
    db
):
    creditors = []
    debtors = []

    for participant_id, balance in balances.items():

        if balance > 0:
            creditors.append(
                [participant_id, balance]
            )

        elif balance < 0:
            debtors.append(
                [participant_id, abs(balance)]
            )

    settlements = []

    creditor_index = 0
    debtor_index = 0

    while (
        creditor_index < len(creditors)
        and debtor_index < len(debtors)
    ):

        creditor_id, credit = (
            creditors[creditor_index]
        )

        debtor_id, debt = (
            debtors[debtor_index]
        )

        payment = min(
            credit,
            debt
        )

        debtor = (
            db.query(Participant)
            .filter(
                Participant.id == debtor_id
            )
            .first()
        )

        creditor = (
            db.query(Participant)
            .filter(
                Participant.id == creditor_id
            )
            .first()
        )

        settlements.append(
            {
                "from": debtor.name,
                "to": creditor.name,
                "amount": round(payment, 2)
            }
        )

        creditors[creditor_index][1] -= payment
        debtors[debtor_index][1] -= payment

        if creditors[creditor_index][1] == 0:
            creditor_index += 1

        if debtors[debtor_index][1] == 0:
            debtor_index += 1

    return settlements
