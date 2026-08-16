def create_holiday(client, auth_headers):
    response = client.post(
        "/holidays/",
        headers=auth_headers,
        json={
            "name": "Test Holiday"
        }
    )

    return response.json()["id"]


def create_participant(
    client,
    name,
    holiday_id
):
    response = client.post(
        "/participants/",
        json={
            "name": name,
            "holiday_id": holiday_id
        }
    )

    return response.json()["id"]


def create_expense_test_data(
    client,
    auth_headers
):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    participant_1 = create_participant(
        client,
        "Natasha",
        holiday_id
    )

    participant_2 = create_participant(
        client,
        "Tom",
        holiday_id
    )

    return (
        holiday_id,
        participant_1,
        participant_2
    )


def test_create_expense(client, auth_headers):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    response = client.post(
        "/expenses/",
        json={
            "description": "Dinner",
            "amount": 50,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] > 0

    assert (
        data["description"]
        == "Dinner"
    )

    assert float(
        data["amount"]
    ) == 50.0


def test_get_expenses_for_holiday(
    client,
    auth_headers
):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    client.post(
        "/expenses/",
        json={
            "description": "Hotel",
            "amount": 300,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    response = client.get(
        f"/expenses/holiday/{holiday_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) >= 1

    assert (
        data[0]["holiday_id"]
        == holiday_id
    )


def test_update_expense(client, auth_headers):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    create_response = client.post(
        "/expenses/",
        json={
            "description": "Lunch",
            "amount": 20,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1
            ]
        }
    )

    expense_id = (
        create_response
        .json()["id"]
    )

    update_response = client.put(
        f"/expenses/{expense_id}",
        json={
            "description": "Dinner",
            "amount": 80,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_2,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    assert (
        update_response.status_code
        == 200
    )

    data = (
        update_response.json()
    )

    assert (
        data["description"]
        == "Dinner"
    )

    assert float(
        data["amount"]
    ) == 80.0

    assert (
        data[
            "paid_by_participant_id"
        ]
        == participant_2
    )


def test_delete_expense(client, auth_headers):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    create_response = client.post(
        "/expenses/",
        json={
            "description": "Delete Me",
            "amount": 25,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    expense_id = (
        create_response
        .json()["id"]
    )

    response = client.delete(
        f"/expenses/{expense_id}"
    )

    assert response.status_code == 200

    assert (
        response.json()["message"]
        == "Expense deleted"
    )


def test_negative_amount_rejected(
    client,
    auth_headers
):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    response = client.post(
        "/expenses/",
        json={
            "description": "Dinner",
            "amount": -50,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    assert response.status_code == 422


def test_zero_amount_rejected(
    client,
    auth_headers
):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    response = client.post(
        "/expenses/",
        json={
            "description": "Dinner",
            "amount": 0,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    assert response.status_code == 422


def test_delete_nonexistent_expense_returns_404(
    client,
    auth_headers
):
    response = client.delete(
        "/expenses/999999"
    )

    assert response.status_code == 404

    assert (
        response.json()["detail"]
        == "Expense not found"
    )


def test_update_nonexistent_expense_returns_404(
    client,
    auth_headers
):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    response = client.put(
        "/expenses/999999",
        json={
            "description": "Test",
            "amount": 10,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    assert response.status_code == 404

    assert (
        response.json()["detail"]
        == "Expense not found"
    )


def test_get_expense_participants(
    client,
    auth_headers
):
    (
        holiday_id,
        participant_1,
        participant_2
    ) = create_expense_test_data(
        client,
        auth_headers
    )

    create_response = client.post(
        "/expenses/",
        json={
            "description": "Split Test",
            "amount": 45,
            "holiday_id": holiday_id,
            "paid_by_participant_id": participant_1,
            "participant_ids": [
                participant_1,
                participant_2
            ]
        }
    )

    expense_id = (
        create_response
        .json()["id"]
    )

    response = client.get(
        f"/expenses/{expense_id}/participants"
    )

    assert response.status_code == 200

    data = response.json()

    assert participant_1 in data

    assert participant_2 in data

    assert len(data) == 2