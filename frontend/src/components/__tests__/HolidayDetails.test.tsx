import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";

import HolidayDetails from "../../pages/HolidayDetails";
import {
    describe,
    test,
    expect
} from "vitest";
describe(
    "HolidayDetails",
    () => {
        test(
            "shows loading state",
            () => {
                render(
                    <MemoryRouter>
                        <HolidayDetails />
                    </MemoryRouter>
                );

                expect(
                    screen.getByText(
                        /loading/i
                    )
                ).toBeInTheDocument();
            }
        );
    }
);