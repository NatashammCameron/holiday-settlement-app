import { useEffect, useState } from "react";
import type { Holiday } from "../types/Holiday";
import { Link } from "react-router-dom";
import {
    getHolidays,
    createHoliday
} from "../services/holidayService";

function Dashboard() {
    const [holidays, setHolidays] = useState<Holiday[]>([]);
    const [holidayName, setHolidayName] = useState("");

    useEffect(() => {
        async function loadHolidays() {
            try {
                const data = await getHolidays();

                console.log("HOLIDAYS:", data);

                setHolidays(data);
            } catch (error) {
                console.error(
                    "Failed to load holidays:",
                    error
                );
            }
        }

        loadHolidays();
    }, []);

    async function handleCreateHoliday() {
        if (!holidayName.trim()) {
            return;
        }

        try {
            await createHoliday(holidayName);

            const updatedHolidays =
                await getHolidays();

            setHolidays(updatedHolidays);

            setHolidayName("");
        } catch (error) {
            console.error(
                "Failed to create holiday:",
                error
            );
        }
    }

    return (
        <div className="container">
            <h1>Holiday Settlement App</h1>

            <div>
                <input
                    type="text"
                    placeholder="Holiday name"
                    value={holidayName}
                    onChange={(e) =>
                        setHolidayName(
                            e.target.value
                        )
                    }
                />

                <button
                    onClick={handleCreateHoliday}
                >
                    Create Holiday
                </button>
            </div>

            <h2>Your Holidays</h2>

            <div className="holiday-list">
                {holidays.map((holiday) => (
                    <Link
                        to={`/holiday/${holiday.id}`}
                        key={holiday.id}
                        className="holiday-card"
                    >
                        {holiday.name}
                    </Link>

                ))}
            </div>
        </div>
    );
}

export default Dashboard;