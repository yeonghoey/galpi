from http import HTTPStatus


def test_user(client, user):
    client.get(f'/{user}')
    assert client.json == {'item': {}, 'children': []}

    client.put(f'/{user}/a', data={'to': 'A'})
    assert client.status == HTTPStatus.CREATED
    assert client.json is None
