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

export async function getHoliday(
    holidayId: string
): Promise<Holiday> {
    const response = await fetch(
        `http://127.0.0.1:8000/holidays/${holidayId}`
    );

    if (!response.ok) {
        throw new Error(
            "Failed to fetch holiday"
        );
    }

    return response.json();
}

export async function updateHoliday(
    holidayId: string,
    name: string
): Promise<void> {
    const response = await fetch(
        `http://127.0.0.1:8000/holidays/${holidayId}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name
            })
        }
    );

    if (!response.ok) {
        throw new Error(
            "Failed to update holiday"
        );
    }
}

export async function deleteHoliday(
    holidayId: string
): Promise<void> {
    const response = await fetch(
        `http://127.0.0.1:8000/holidays/${holidayId}`,
        {
            method: "DELETE"
        }
    );

    if (!response.ok) {
        throw new Error(
            "Failed to delete holiday"
        );
    }
}