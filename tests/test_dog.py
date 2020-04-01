def test_dog_get(client):
    response = client.get("/v1/dog/")
    assert response.status_code == 200


def test_dog_get_by_id(client):
    response = client.get("/v1/dog/1")
    assert response.status_code == 404
