def test_user(client, user):
    client.get(f'/{user}', follow_redirects=True)
    assert client.last == {
        'item': {},
        'children': []
    }
