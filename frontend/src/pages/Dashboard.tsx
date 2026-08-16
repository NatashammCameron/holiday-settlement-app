import { useEffect, useState } from "react";
import type { Holiday } from "../types/Holiday";
import { Link } from "react-router-dom";
import "../styles/Dashboard.css";
import {
    getHolidays,
    createHoliday
} from "../services/holidayService";
import LogoutButton from "../components/LogoutButton";
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
        <div className="dashboard-page">
            <div className="container">
                <header className="dashboard-hero">
                    <p className="dashboard-eyebrow">Trip Ledger</p>
                    <h1 className="dashboard-title">
                        Holiday Settlement
                    </h1>
                    <LogoutButton />
                   
                </header>

                <div className="new-holiday-form">
                    <input
                        type="text"
                        className="text-input"
                        placeholder="Holiday name"
                        value={holidayName}
                        onChange={(e) =>
                            setHolidayName(
                                e.target.value
                            )
                        }
                    />
                    <button
                        className="btn"
                        onClick={handleCreateHoliday}
                    >
                        Create Holiday
                    </button>
                </div>

                <h2>Your Holidays</h2>

                {holidays.length === 0 ? (
                    <p className="dashboard-empty">
                        No holidays yet — add one above to start splitting
                        costs.
                    </p>
                ) : (
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
                )}
            </div>
        </div>
    );
}

export default Dashboard;
