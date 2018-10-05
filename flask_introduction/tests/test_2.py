
import pytest
import json

def test_empty_db(client):
    response = client.get('/getJson')
    r = json.loads(response.data)

    assert r["name"] == 'nishant'