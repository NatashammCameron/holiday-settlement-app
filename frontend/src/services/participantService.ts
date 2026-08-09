import type { Participant } from "../types/Participant";

export async function getParticipants(
    holidayId: string
): Promise<Participant[]> {
    const response = await fetch(
        `http://127.0.0.1:8000/participants/holiday/${holidayId}`
    );

    if (!response.ok) {
        throw new Error(
            "Failed to fetch participants"
        );
    }

    return response.json();
}

export async function createParticipant(
    name: string,
    holidayId: string
): Promise<void> {
    const response = await fetch(
        "http://127.0.0.1:8000/participants/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                holiday_id: Number(holidayId)
            })
        }
    );

    if (!response.ok) {
        throw new Error(
            "Failed to create participant"
        );
    }
}