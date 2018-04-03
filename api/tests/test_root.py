import json


def test_user(client, user):
    response = client.get(f'/{user}', follow_redirects=True)
    assert json.loads(response.data) == {
        'item': {},
        'children': []
    }
