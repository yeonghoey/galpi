from http import HTTPStatus


def test_user(client, user):
    client.get(f'/{user}')
    assert client.status == HTTPStatus.OK
    assert client.json == {'item': {}, 'children': []}

    client.put(f'/{user}/a', json={'to': 'http://example.com'})
    assert client.status == HTTPStatus.CREATED
    assert client.json is None

    client.get(f'/{user}')
    assert client.status == HTTPStatus.OK
    assert client.json == {
        'item': {},
        'children': [
            {
                'owner': user,
                'name': 'a',
                'to': 'http://example.com',
            }
        ]
    }


def test_pq(client, user):
    items = client.batch_put(user, '''
    a     | a.com
    a/1   | a1.com
    a/2   | a2.com
    a/b/1 | ab1.com
    a/b/2 | ab2.com
    x/y/z | xyz.com''')

    client.get(f'/{user}', ok=True)
    client.get(f'/{user}/', ok=True)
    assert client[-1].json == client.json
    assert client.json == {
        'item': {},
        'children': list(items.values())
    }
