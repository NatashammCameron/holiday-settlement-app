import type { Settlement } from "../types/Settlement";

export async function getSettlements(
    holidayId: string
): Promise<Settlement[]> {
    const response = await fetch(
        `http://127.0.0.1:8000/settlements/holiday/${holidayId}/payments`
    );

    if (!response.ok) {
        throw new Error(
            "Failed to fetch settlements"
        );
    }

    return response.json();
}