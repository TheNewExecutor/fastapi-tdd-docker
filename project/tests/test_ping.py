# project/tests/test_ping.py


def test_ping(test_app):
    # Given
    # test app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
