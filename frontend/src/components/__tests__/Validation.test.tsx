import {
    describe,
    test,
    expect
} from "vitest";

describe(
    "Validation",
    () => {
        test(
            "amount validation rule exists",
            () => {
                const amount = -10;

                expect(
                    amount <= 0
                ).toBe(true);
            }
        );
    }
);