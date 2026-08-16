def create_holiday(client, auth_headers):
    response = client.post(
        "/holidays/",
        headers=auth_headers,
        json={
            "name": "Test Holiday"
        }
    )

    return response.json()["id"]


def test_create_participant(client, auth_headers):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    response = client.post(
        "/participants/",
        json={
            "name": "Natasha",
            "holiday_id": holiday_id
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] > 0
    assert data["name"] == "Natasha"
    assert data["holiday_id"] == holiday_id


def test_get_participants_for_holiday(
    client,
    auth_headers
):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    client.post(
        "/participants/",
        json={
            "name": "Natasha",
            "holiday_id": holiday_id
        }
    )

    client.post(
        "/participants/",
        json={
            "name": "Tom",
            "holiday_id": holiday_id
        }
    )

    response = client.get(
        f"/participants/holiday/{holiday_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2


def test_update_participant(client, auth_headers):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    create_response = client.post(
        "/participants/",
        json={
            "name": "Old Name",
            "holiday_id": holiday_id
        }
    )

    participant_id = (
        create_response.json()["id"]
    )

    update_response = client.put(
        f"/participants/{participant_id}",
        json={
            "name": "New Name",
            "holiday_id": holiday_id
        }
    )

    assert update_response.status_code == 200

    assert (
        update_response.json()["name"]
        == "New Name"
    )


def test_delete_participant(client, auth_headers):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    create_response = client.post(
        "/participants/",
        json={
            "name": "Delete Me",
            "holiday_id": holiday_id
        }
    )

    participant_id = (
        create_response.json()["id"]
    )

    delete_response = client.delete(
        f"/participants/{participant_id}"
    )

    assert delete_response.status_code == 200

    assert (
        delete_response.json()["message"]
        == "Participant deleted"
    )


def test_update_nonexistent_participant(
    client,
    auth_headers
):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    response = client.put(
        "/participants/999999",
        json={
            "name": "Ghost",
            "holiday_id": holiday_id
        }
    )

    assert response.status_code == 404


def test_delete_nonexistent_participant(
    client,
    auth_headers
):
    response = client.delete(
        "/participants/999999"
    )

    assert response.status_code == 404


def test_empty_participant_name_rejected(
    client,
    auth_headers
):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    response = client.post(
        "/participants/",
        json={
            "name": "",
            "holiday_id": holiday_id
        }
    )

    assert response.status_code == 422


def test_participant_name_too_long_rejected(
    client,
    auth_headers
):
    holiday_id = create_holiday(
        client,
        auth_headers
    )

    response = client.post(
        "/participants/",
        json={
            "name": "A" * 51,
            "holiday_id": holiday_id
        }
    )

    assert response.status_code == 422