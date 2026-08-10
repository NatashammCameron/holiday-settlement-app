def test_delete_holiday_cascades_related_records(
    client
):
    holiday_response = client.post(
        "/holidays/",
        json={
            "name": "Cascade Test"
        }
    )

    holiday_id = (
        holiday_response
        .json()["id"]
    )

    participant_1 = client.post(
        "/participants/",
        json={
            "name": "Natasha",
            "holiday_id": holiday_id
        }
    ).json()["id"]

    participant_2 = client.post(
        "/participants/",
        json={
            "name": "Tom",
            "holiday_id": holiday_id
        }
    ).json()["id"]

    expense_response = client.post(
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

    expense_id = (
        expense_response
        .json()["id"]
    )

    delete_response = client.delete(
        f"/holidays/{holiday_id}"
    )

    assert (
        delete_response.status_code
        == 200
    )

    holiday_check = client.get(
        f"/holidays/{holiday_id}"
    )

    assert (
        holiday_check.status_code
        == 404
    )

    participants_check = client.get(
        f"/participants/holiday/{holiday_id}"
    )

    assert (
        participants_check.status_code
        == 200
    )

    assert (
        participants_check.json()
        == []
    )

    expenses_check = client.get(
        f"/expenses/holiday/{holiday_id}"
    )

    assert (
        expenses_check.status_code
        == 200
    )

    assert (
        expenses_check.json()
        == []
    )

    expense_participants_check = (
        client.get(
            f"/expenses/{expense_id}/participants"
        )
    )

    assert (
        expense_participants_check
        .status_code
        == 200
    )

    assert (
        expense_participants_check.json()
        == []
    )