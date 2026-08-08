import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import type { Holiday } from "../types/Holiday";
import { getHoliday } from "../services/holidayService";

function HolidayDetails() {
    const { id } = useParams();

    const [holiday, setHoliday] =
        useState<Holiday | null>(null);

    useEffect(() => {
        async function loadHoliday() {
            if (!id) {
                return;
            }

            const data = await getHoliday(id);

            setHoliday(data);
        }

        loadHoliday();
    }, [id]);

    if (!holiday) {
        return <p>Loading...</p>;
    }

    return (
        <div className="container">
            <h1>{holiday.name}</h1>

            <p>
                Holiday ID: {holiday.id}
            </p>

            <h2>Participants</h2>

            <p>No participants yet</p>

            <h2>Expenses</h2>

            <p>No expenses yet</p>

            <h2>Settlements</h2>

            <p>No settlements yet</p>
        </div>
    );
}

export default HolidayDetails;