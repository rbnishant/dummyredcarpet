import pytest

def test_empty_db(client)
    response = client.get('/')
    assert response.data.find(b'request-info') > 0
