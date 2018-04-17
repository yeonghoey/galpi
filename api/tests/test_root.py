from http import HTTPStatus


def test_get_all(client, user):
    client.session({'user': user})
    client.put(f'/{user}/a', json={'link': 'a.com'}, ok=True)
    client.put(f'/{user}/b', json={'link': 'b.com'}, ok=True)

    # Both are vaild
    client.get(f'/{user}')
    client.get(f'/{user}/')
    assert client[-1].json == client.json == [
        {'user': user, 'name': 'a', 'link': 'a.com'},
        {'user': user, 'name': 'b', 'link': 'b.com'},
    ]


def test_put_item_overwrites(client, user):
    client.session({'user': user})
    client.put(f'/{user}/a', json={'link': 'a.com'}, ok=True)
    client.put(f'/{user}/a', json={'link': 'a.org'}, ok=True)
    client.get(f'/{user}/a')
    assert client.json == {'user': user, 'name': 'a', 'link': 'a.org'}


def test_put_item_owner_only(client, user):
    client.session({'user': None})
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    client.session({'user': 'NOT_OWNER'})
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    client.session({'user': user})
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.CREATED
