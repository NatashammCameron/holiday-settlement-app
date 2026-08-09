import type { Expense } from "../types/Expense";

export async function getExpenses(
    holidayId: string
): Promise<Expense[]> {
    const response = await fetch(
        `http://127.0.0.1:8000/expenses/holiday/${holidayId}`
    );

    if (!response.ok) {
        throw new Error("Failed to fetch expenses");
    }

    return response.json();
}

export async function createExpense(
    description: string,
    amount: number,
    holidayId: string,
    paidByParticipantId: number
): Promise<void> {
    const response = await fetch(
        "http://127.0.0.1:8000/expenses/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                description,
                amount,
                holiday_id: Number(holidayId),
                paid_by_participant_id:
                    paidByParticipantId,
                participant_ids: [
                    paidByParticipantId
                ]
            
            })
        }
    );

    if (!response.ok) {
        throw new Error("Failed to create expense");
    }
}