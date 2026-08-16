import type { Holiday } from "../types/Holiday";

const API_URL = "http://127.0.0.1:8000";

function getAuthHeaders() {
    const token = localStorage.getItem("token");

    return {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`
    };
}

export async function getHolidays(): Promise<Holiday[]> {
    const response = await fetch(
        `${API_URL}/holidays/`,
        {
            headers: getAuthHeaders()
        }
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
        `${API_URL}/holidays/`,
        {
            method: "POST",
            headers: getAuthHeaders(),
            body: JSON.stringify({
                name
            })
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
        `${API_URL}/holidays/${holidayId}`,
        {
            headers: getAuthHeaders()
        }
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
        `${API_URL}/holidays/${holidayId}`,
        {
            method: "PUT",
            headers: getAuthHeaders(),
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
        `${API_URL}/holidays/${holidayId}`,
        {
            method: "DELETE",
            headers: getAuthHeaders()
        }
    );

    if (!response.ok) {
        throw new Error(
            "Failed to delete holiday"
        );
    }
}