import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import type { Holiday } from "../types/Holiday";
import { getHoliday } from "../services/holidayService";

import type { Participant } from "../types/Participant";

import {
    getParticipants,
    createParticipant
} from "../services/participantService";

import type { Expense } from "../types/Expense";

import {
    getExpenses,
    createExpense
} from "../services/expenseService";

function HolidayDetails() {
    const { id } = useParams();

    const [holiday, setHoliday] =
        useState<Holiday | null>(null);

    const [participants, setParticipants] =
        useState<Participant[]>([]);

    const [participantName, setParticipantName] =
        useState("");

    const [expenses, setExpenses] =
        useState<Expense[]>([]);

    const [description, setDescription] =
        useState("");

    const [amount, setAmount] =
        useState("");

    const [paidBy, setPaidBy] =
        useState("");

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

    useEffect(() => {
        async function loadParticipants() {
            if (!id) {
                return;
            }

            const data =
                await getParticipants(id);

            setParticipants(data);
        }

        loadParticipants();
    }, [id]);

    useEffect(() => {
        async function loadExpenses() {
            if (!id) {
                return;
            }

            const data =
                await getExpenses(id);

            setExpenses(data);
        }

        loadExpenses();
    }, [id]);

    async function handleCreateParticipant() {
        if (!id || !participantName.trim()) {
            return;
        }

        await createParticipant(
            participantName,
            id
        );

        const updatedParticipants =
            await getParticipants(id);

        setParticipants(updatedParticipants);

        setParticipantName("");
    }

    async function handleCreateExpense() {
        if (
            !id ||
            !description ||
            !amount ||
            !paidBy
        ) {
            return;
        }

        await createExpense(
            description,
            Number(amount),
            id,
            Number(paidBy)
        );

        const updatedExpenses =
            await getExpenses(id);

        setExpenses(updatedExpenses);

        setDescription("");
        setAmount("");
        setPaidBy("");
    }

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

            <input
                type="text"
                placeholder="Participant name"
                value={participantName}
                onChange={(e) =>
                    setParticipantName(
                        e.target.value
                    )
                }
            />

            <button
                onClick={
                    handleCreateParticipant
                }
            >
                Add Participant
            </button>

            <ul>
                {participants.map(
                    (participant) => (
                        <li
                            key={participant.id}
                        >
                            {participant.name}
                        </li>
                    )
                )}
            </ul>

            <h2>Expenses</h2>

            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) =>
                    setDescription(
                        e.target.value
                    )
                }
            />

            <input
                type="number"
                placeholder="Amount"
                value={amount}
                onChange={(e) =>
                    setAmount(
                        e.target.value
                    )
                }
            />

            <select
                value={paidBy}
                onChange={(e) =>
                    setPaidBy(
                        e.target.value
                    )
                }
            >
                <option value="">
                    Select payer
                </option>

                {participants.map(
                    (participant) => (
                        <option
                            key={participant.id}
                            value={
                                participant.id
                            }
                        >
                            {participant.name}
                        </option>
                    )
                )}
            </select>

            <button
                onClick={
                    handleCreateExpense
                }
            >
                Add Expense
            </button>

            <ul>
                {expenses.map((expense) => (
                    <li key={expense.id}>
                        {expense.description} - £
                        {expense.amount}
                    </li>
                ))}
            </ul>

            <h2>Settlements</h2>

            <p>No settlements yet</p>
        </div>
    );
}

export default HolidayDetails;