def test_create_holiday(client):
    response = client.post(
        "/holidays/",
        json={
            "name": "Paris Trip"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] > 0
    assert data["name"] == "Paris Trip"


def test_get_holiday(client):
    create_response = client.post(
        "/holidays/",
        json={
            "name": "Spain Trip"
        }
    )

    holiday_id = (
        create_response.json()["id"]
    )

    response = client.get(
        f"/holidays/{holiday_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == holiday_id
    assert data["name"] == "Spain Trip"


def test_get_all_holidays(client):
    client.post(
        "/holidays/",
        json={
            "name": "Holiday One"
        }
    )

    client.post(
        "/holidays/",
        json={
            "name": "Holiday Two"
        }
    )

    response = client.get(
        "/holidays/"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(
        data,
        list
    )

    assert len(data) >= 2


def test_update_holiday(client):
    create_response = client.post(
        "/holidays/",
        json={
            "name": "Old Name"
        }
    )

    holiday_id = (
        create_response.json()["id"]
    )

    update_response = client.put(
        f"/holidays/{holiday_id}",
        json={
            "name": "New Name"
        }
    )

    assert update_response.status_code == 200

    updated_data = (
        update_response.json()
    )

    assert (
        updated_data["name"]
        == "New Name"
    )

    get_response = client.get(
        f"/holidays/{holiday_id}"
    )

    assert (
        get_response.json()["name"]
        == "New Name"
    )


def test_delete_holiday(client):
    create_response = client.post(
        "/holidays/",
        json={
            "name": "Delete Me"
        }
    )

    holiday_id = (
        create_response.json()["id"]
    )

    delete_response = client.delete(
        f"/holidays/{holiday_id}"
    )

    assert delete_response.status_code == 200

    assert (
        delete_response.json()["message"]
        == "Holiday deleted"
    )

    get_response = client.get(
    f"/holidays/{holiday_id}"
)

    assert (
        get_response.status_code
        == 404
    )

    assert (
        get_response.json()["detail"]
        == "Holiday not found"
    )


def test_update_nonexistent_holiday_returns_404(
    client
):
    response = client.put(
        "/holidays/999999",
        json={
            "name": "New Name"
        }
    )

    assert response.status_code == 404

    data = response.json()

    assert (
        data["detail"]
        == "Holiday not found"
    )


def test_delete_nonexistent_holiday_returns_404(
    client
):
    response = client.delete(
        "/holidays/999999"
    )

    assert response.status_code == 404

    data = response.json()

    assert (
        data["detail"]
        == "Holiday not found"
    )


def test_empty_holiday_name_rejected(
    client
):
    response = client.post(
        "/holidays/",
        json={
            "name": ""
        }
    )

    assert response.status_code == 422


def test_holiday_name_too_long_rejected(
    client
):
    response = client.post(
        "/holidays/",
        json={
            "name": "A" * 101
        }
    )

    assert response.status_code == 422


def test_updated_holiday_name_too_long_rejected(
    client
):
    create_response = client.post(
        "/holidays/",
        json={
            "name": "Valid Name"
        }
    )

    holiday_id = (
        create_response.json()["id"]
    )

    response = client.put(
        f"/holidays/{holiday_id}",
        json={
            "name": "A" * 101
        }
    )

    assert response.status_code == 422