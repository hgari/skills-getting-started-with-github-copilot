def test_get_activities_returns_activity_catalog(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_has_expected_shape(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    payload = response.json()

    for _, activity in payload.items():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
