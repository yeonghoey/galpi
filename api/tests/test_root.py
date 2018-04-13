from http import HTTPStatus


def test_pq(client, username):
    items = client.batch_put(username, '''
    a     | a.com
    a/1   | a1.com
    a/2   | a2.com
    a/b/1 | ab1.com
    a/b/2 | ab2.com
    x/y/z | xyz.com''')

    client.get(f'/{username}', ok=True)
    client.get(f'/{username}/', ok=True)
    assert client[-1].json == client.json
    assert client.json == {
        'self': {},
        'children': list(items.values())
    }

    # Requests a redirect query, (so returns no children)
    client.get(f'/{username}/a', ok=True)
    assert client.json == {'self': items['a'], 'children': []}

    # Requests a list query, includes the item itself
    client.get(f'/{username}/a/', ok=True)
    assert client.json == {
        'self': items['a'],
        'children': [items[n] for n in 'a/1;a/2;a/b/1;a/b/2'.split(';')]
    }

    # Requests a redirect query, but fallback to a list query
    client.get(f'/{username}/a/b', ok=True)
    client.get(f'/{username}/a/b/', ok=True)
    assert (client[-1].json ==
            client.json == {
                'self': {},
                'children': [items[n] for n in 'a/b/1;a/b/2'.split(';')]
            })

    # Same goes even if the direct child does not exist
    client.get(f'/{username}/x', ok=True)
    client.get(f'/{username}/x/', ok=True)
    client.get(f'/{username}/x/y', ok=True)
    client.get(f'/{username}/x/y/', ok=True)
    assert (client[-3].json ==
            client[-2].json ==
            client[-1].json ==
            client.json == {
                'self': {},
                'children': [items['x/y/z']]
            })


def test_put(client, username):
    client.put(f'/{username}/a', json={'linkto': 'http://example.com'})
    assert client.status == HTTPStatus.CREATED
    assert client.json is None
