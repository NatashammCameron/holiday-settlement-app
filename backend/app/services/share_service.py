from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit


def calculate_expense_share(
    expense: Expense,
    split_count: int
):
    return float(expense.amount) / split_count