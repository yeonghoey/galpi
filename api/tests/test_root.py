def test_user(client, user):
    client.get(f'/{user}')
    assert client.last == {
        'item': {},
        'children': []
    }
