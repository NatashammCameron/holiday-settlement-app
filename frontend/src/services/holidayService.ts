import type { Holiday } from "../types/Holiday";

export async function getHolidays(): Promise<Holiday[]> {
    const response = await fetch(
        "http://127.0.0.1:8000/holidays/"
    );

    if (!response.ok) {
        throw new Error("Failed to fetch holidays");
    }

    return response.json();
}

export async function createHoliday(
    name: string
): Promise<void> {
    const response = await fetch(
        "http://127.0.0.1:8000/holidays/",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
            }),
        }
    );

    if (!response.ok) {
        throw new Error("Failed to create holiday");
    }
}