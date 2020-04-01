def test_cat_get(client):
    response = client.get("/v1/cat/")
    assert response.status_code == 200


def test_cat_get_by_id(client):
    response = client.get("/v1/cat/1")
    assert response.status_code == 404
