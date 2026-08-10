import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import "../styles/HolidayDetails.css";
import type { Holiday } from "../types/Holiday";
import {
    getHoliday,
    updateHoliday,
    deleteHoliday
} from "../services/holidayService";

import type { Participant } from "../types/Participant";

import {
    getParticipants,
    createParticipant,
    deleteParticipant,
    updateParticipant
} from "../services/participantService";

import type { Expense } from "../types/Expense";

import {
    getExpenses,
    createExpense,
    deleteExpense,
    updateExpense,
    getExpenseParticipants
} from "../services/expenseService";

import type { Settlement } from "../types/Settlement";

import {
    getSettlements
} from "../services/settlementService";

function HolidayDetails() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [holiday, setHoliday] =
        useState<Holiday | null>(null);

    const [participants, setParticipants] =
        useState<Participant[]>([]);

    const [participantName, setParticipantName] =
        useState("");

    const [expenses, setExpenses] =
        useState<Expense[]>([]);

    const [settlements, setSettlements] =
        useState<Settlement[]>([]);

    const [description, setDescription] =
        useState("");

    const [amount, setAmount] =
        useState("");

    const [paidBy, setPaidBy] =
        useState("");

    const [selectedParticipants, setSelectedParticipants] =
        useState<number[]>([]);

    const [editingExpenseId, setEditingExpenseId] =
        useState<number | null>(null);

    const [editDescription, setEditDescription] =
        useState("");

    const [editAmount, setEditAmount] =
        useState("");

    const [editPaidBy, setEditPaidBy] =
        useState("");

    const [
        editSelectedParticipants,
        setEditSelectedParticipants
    ] = useState<number[]>([]);

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

    useEffect(() => {
        async function loadSettlements() {
            if (!id) {
                return;
            }

            const data =
                await getSettlements(id);

            setSettlements(data);
        }

        loadSettlements();
    }, [id]);

    async function handleCreateParticipant() {
        if (!id) {
            return;
        }

        if (!participantName.trim()) {
            alert(
                "Participant name is required"
            );
            return;
        }

        const exists =
            participants.some(
                (participant) =>
                    participant.name
                        .toLowerCase()
                        .trim() ===
                    participantName
                        .toLowerCase()
                        .trim()
            );

        if (exists) {
            alert(
                "Participant already exists"
            );

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

    function handleBackToDashboard() {
        navigate("/");
    }
    async function handleEditParticipant(
        participant: Participant
    ) {
        if (!id) {
            return;
        }

        const newName = prompt(
            "Enter new participant name",
            participant.name
        );

        if (!newName?.trim()) {
            return;
        }

        await updateParticipant(
            participant.id,
            newName,
            id
        );

        const updatedParticipants =
            await getParticipants(id);

        setParticipants(updatedParticipants);
    }

    async function handleDeleteParticipant(
        participantId: number
    ) {
        if (!id) {
            return;
        }

        try {
            await deleteParticipant(
                participantId
            );

            const updatedParticipants =
                await getParticipants(id);

            setParticipants(
                updatedParticipants
            );
        } catch (error) {
            alert(
                error instanceof Error
                    ? error.message
                    : "Failed to delete participant"
            );
        }
    }

    async function handleCreateExpense() {
        if (!id) {
            return;
        }

        if (!description.trim()) {
            alert(
                "Description is required"
            );
            return;
        }

        if (!amount) {
            alert(
                "Amount is required"
            );
            return;
        }

        if (Number(amount) <= 0) {
            alert(
                "Amount must be greater than zero"
            );
            return;
        }

        if (!paidBy) {
            alert(
                "Please select a payer"
            );
            return;
        }

        if (
            selectedParticipants.length === 0
        ) {
            alert(
                "Select at least one participant"
            );
            return;
        }

        await createExpense(
            description,
            Number(amount),
            id,
            Number(paidBy),
            selectedParticipants
        );

        const updatedExpenses =
            await getExpenses(id);

        setExpenses(updatedExpenses);

        const updatedSettlements =
            await getSettlements(id);

        setSettlements(updatedSettlements);

        setDescription("");
        setAmount("");
        setPaidBy("");
        setSelectedParticipants([]);
    }

    async function handleEditExpense(
        expense: Expense
    ) {
        if (!id) {
            return;
        }

        const participantIds =
            await getExpenseParticipants(
                expense.id
            );

        setEditingExpenseId(
            expense.id
        );

        setEditDescription(
            expense.description
        );

        setEditAmount(
            expense.amount.toString()
        );

        setEditPaidBy(
            expense.paid_by_participant_id.toString()
        );

        setEditSelectedParticipants(
            participantIds
        );
    }

    async function handleSaveExpenseEdit() {
        if (
            !id ||
            editingExpenseId === null
        ) {
            return;
        }

        await updateExpense(
            editingExpenseId,
            editDescription,
            Number(editAmount),
            id,
            Number(editPaidBy),
            editSelectedParticipants
        );

        const updatedExpenses =
            await getExpenses(id);

        setExpenses(updatedExpenses);

        const updatedSettlements =
            await getSettlements(id);

        setSettlements(updatedSettlements);

        setEditingExpenseId(null);

        setEditDescription("");
        setEditAmount("");
        setEditPaidBy("");
        setEditSelectedParticipants([]);
    }

    async function handleEditHoliday() {
        if (!id || !holiday) {
            return;
        }

        const newName = prompt(
            "Enter holiday name",
            holiday.name
        );

        if (!newName?.trim()) {
            return;
        }

        await updateHoliday(
            id,
            newName
        );

        const updatedHoliday =
            await getHoliday(id);

        setHoliday(updatedHoliday);
    }

    async function handleDeleteHoliday() {
        if (!id) {
            return;
        }

        const confirmed =
            window.confirm(
                "Delete this holiday?"
            );

        if (!confirmed) {
            return;
        }

        await deleteHoliday(id);

        window.location.href = "/";
    }
    async function handleDeleteExpense(
        expenseId: number
    ) {
        if (!id) {
            return;
        }

        await deleteExpense(expenseId);

        const updatedExpenses =
            await getExpenses(id);

        setExpenses(updatedExpenses);

        const updatedSettlements =
            await getSettlements(id);

        setSettlements(updatedSettlements);
    }

    if (!holiday) {
        return (
            <div className="holiday-page">
                <p className="holiday-loading">Loading…</p>
            </div>
        );
    }

    return (
        <div className="holiday-page">
            <div className="container">
                <header className="holiday-header">
                    <div className="holiday-actions">

                        <button
                            onClick={handleBackToDashboard}
                        >
                            ← Dashboard
                        </button>

                        <button
                            onClick={handleEditHoliday}
                            className="edit-button"
                        >
                            Edit Holiday
                        </button>

                        <button
                            onClick={handleDeleteHoliday}
                            className="delete-button"
                        >
                            Delete Holiday
                        </button>

                    </div>
                    <div>
                        <p className="eyebrow">Trip Ledger</p>
                        <h1 className="holiday-title">{holiday.name}</h1>
                        <p className="holiday-id">Holiday ID: {holiday.id}</p>
                    </div>

                    <div className="holiday-actions">
                        <button
                            onClick={handleEditHoliday}
                            className="btn edit-button"
                        >
                            Edit Holiday
                        </button>

                        <button
                            onClick={handleDeleteHoliday}
                            className="btn delete-button"
                        >
                            Delete Holiday
                        </button>
                    </div>
                </header>

                <section className="ledger-section">
                    <h2>Participants</h2>
                    <p className="section-hint">
                        Everyone sharing costs on this trip.
                    </p>

                    <div className="form-row">
                        <input
                            type="text"
                            className="text-input"
                            placeholder="Participant name"
                            value={participantName}
                            onChange={(e) =>
                                setParticipantName(
                                    e.target.value
                                )
                            }
                        />

                        <button
                            className="btn btn-primary"
                            onClick={
                                handleCreateParticipant
                            }
                        >
                            Add Participant
                        </button>
                    </div>

                    <ul className="participant-list">
                        {participants.map(
                            (participant) => (
                                <li
                                    key={participant.id}
                                    className="participant-row"
                                >
                                    <span className="participant-name">
                                        {participant.name}
                                    </span>

                                    <span className="row-actions">
                                        <button
                                            className="btn btn-small"
                                            onClick={() =>
                                                handleEditParticipant(
                                                    participant
                                                )
                                            }
                                        >
                                            Edit
                                        </button>

                                        <button
                                            className="btn btn-small delete-button"
                                            onClick={() =>
                                                handleDeleteParticipant(
                                                    participant.id
                                                )
                                            }
                                        >
                                            Delete
                                        </button>
                                    </span>
                                </li>
                            )
                        )}
                    </ul>
                </section>

                <section className="ledger-section">
                    <h2>Expenses</h2>
                    <p className="section-hint">
                        Log what was spent, who paid, and who it's split between.
                    </p>

                    <div className="form-row">
                        <input
                            type="text"
                            className="text-input"
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
                            className="number-input"
                            placeholder="Amount"
                            value={amount}
                            onChange={(e) =>
                                setAmount(
                                    e.target.value
                                )
                            }
                        />
                    </div>

                    <div className="checkbox-group">
                        <h3>Shared By</h3>

                        <div className="checkbox-row">
                            {participants.map((participant) => (
                                <label
                                    key={participant.id}
                                    className="checkbox-label"
                                >
                                    <input
                                        type="checkbox"
                                        checked={selectedParticipants.includes(
                                            participant.id
                                        )}
                                        onChange={(e) => {
                                            if (e.target.checked) {
                                                setSelectedParticipants([
                                                    ...selectedParticipants,
                                                    participant.id
                                                ]);
                                            } else {
                                                setSelectedParticipants(
                                                    selectedParticipants.filter(
                                                        (id) =>
                                                            id !==
                                                            participant.id
                                                    )
                                                );
                                            }
                                        }}
                                    />

                                    {participant.name}
                                </label>
                            ))}
                        </div>
                    </div>

                    <div className="form-row">
                        <select
                            className="select-input"
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
                                        value={participant.id}
                                    >
                                        {participant.name}
                                    </option>
                                )
                            )}
                        </select>

                        <button
                            className="btn btn-primary"
                            onClick={handleCreateExpense}
                        >
                            Add Expense
                        </button>
                    </div>

                    <ul className="expense-list">
                        {expenses.map((expense) => (
                            <li key={expense.id} className="expense-card">
                                {editingExpenseId === expense.id ? (
                                    <div className="expense-edit-form">
                                        <div className="form-row">
                                            <input
                                                type="text"
                                                className="text-input"
                                                value={editDescription}
                                                onChange={(e) =>
                                                    setEditDescription(
                                                        e.target.value
                                                    )
                                                }
                                            />

                                            <input
                                                type="number"
                                                className="number-input"
                                                value={editAmount}
                                                onChange={(e) =>
                                                    setEditAmount(
                                                        e.target.value
                                                    )
                                                }
                                            />
                                        </div>

                                        <select
                                            className="select-input"
                                            value={editPaidBy}
                                            onChange={(e) =>
                                                setEditPaidBy(
                                                    e.target.value
                                                )
                                            }
                                        >
                                            {participants.map(
                                                (participant) => (
                                                    <option
                                                        key={
                                                            participant.id
                                                        }
                                                        value={
                                                            participant.id
                                                        }
                                                    >
                                                        {
                                                            participant.name
                                                        }
                                                    </option>
                                                )
                                            )}
                                        </select>

                                        <div className="checkbox-group">
                                            <h4>
                                                Shared By
                                            </h4>

                                            <div className="checkbox-row">
                                                {participants.map(
                                                    (participant) => (
                                                        <label
                                                            key={
                                                                participant.id
                                                            }
                                                            className="checkbox-label"
                                                        >
                                                            <input
                                                                type="checkbox"
                                                                checked={editSelectedParticipants.includes(
                                                                    participant.id
                                                                )}
                                                                onChange={(
                                                                    e
                                                                ) => {
                                                                    if (
                                                                        e.target
                                                                            .checked
                                                                    ) {
                                                                        setEditSelectedParticipants(
                                                                            [
                                                                                ...editSelectedParticipants,
                                                                                participant.id
                                                                            ]
                                                                        );
                                                                    } else {
                                                                        setEditSelectedParticipants(
                                                                            editSelectedParticipants.filter(
                                                                                (
                                                                                    id
                                                                                ) =>
                                                                                    id !==
                                                                                    participant.id
                                                                            )
                                                                        );
                                                                    }
                                                                }}
                                                            />

                                                            {
                                                                participant.name
                                                            }
                                                        </label>
                                                    )
                                                )}
                                            </div>
                                        </div>

                                        <div className="expense-edit-actions">
                                            <button
                                                className="btn btn-primary"
                                                onClick={
                                                    handleSaveExpenseEdit
                                                }
                                            >
                                                Save
                                            </button>

                                            <button
                                                className="btn"
                                                onClick={() =>
                                                    setEditingExpenseId(
                                                        null
                                                    )
                                                }
                                            >
                                                Cancel
                                            </button>
                                        </div>
                                    </div>
                                ) : (
                                    <div className="expense-view">
                                        <span className="expense-desc">
                                            {expense.description}
                                        </span>

                                        <span className="expense-amount">
                                            £{expense.amount}
                                        </span>

                                        <span className="row-actions">
                                            <button
                                                className="btn btn-small"
                                                onClick={() =>
                                                    handleEditExpense(
                                                        expense
                                                    )
                                                }
                                            >
                                                Edit
                                            </button>

                                            <button
                                                className="btn btn-small delete-button"
                                                onClick={() =>
                                                    handleDeleteExpense(
                                                        expense.id
                                                    )
                                                }
                                            >
                                                Delete
                                            </button>
                                        </span>
                                    </div>
                                )}
                            </li>
                        ))}
                    </ul>
                </section>

                <section className="ledger-section">
                    <h2>Settlements</h2>
                    <p className="section-hint">
                        Who needs to pay whom to even things out.
                    </p>

                    {settlements.length === 0 ? (
                        <p className="settlement-empty">
                            No settlements yet
                        </p>
                    ) : (
                        <ul className="settlement-list">
                            {settlements.map(
                                (settlement, index) => (
                                    <li
                                        key={index}
                                        className="settlement-stub"
                                    >
                                        <span className="settlement-parties">
                                            <span className="settlement-from">
                                                {settlement.from}
                                            </span>
                                            <span className="settlement-arrow">
                                                →
                                            </span>
                                            <span className="settlement-to">
                                                {settlement.to}
                                            </span>
                                        </span>

                                        <span className="settlement-amount">
                                            £{settlement.amount}
                                        </span>
                                    </li>
                                )
                            )}
                        </ul>
                    )}
                </section>
            </div>
        </div>
    );
}

export default HolidayDetails;
