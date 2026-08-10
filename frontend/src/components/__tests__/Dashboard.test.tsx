import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import Dashboard from "../../pages/Dashboard";
import {
    describe,
    test,
    expect
} from "vitest";

describe("Dashboard", () => {
    test(
        "renders dashboard heading",
        () => {
            render(
                <MemoryRouter>
                    <Dashboard />
                </MemoryRouter>
            );

            expect(
                screen.getByRole(
                    "heading",
                    {
                        name: "Holiday Settlement"
                    }
                )
            ).toBeInTheDocument();
        }
    );
});