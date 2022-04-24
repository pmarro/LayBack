
def test_index_success(client):
    #Page Loads
    response = client.get('/')

    assert response.status_code == 200