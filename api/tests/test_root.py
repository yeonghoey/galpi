from http import HTTPStatus


def me(monkeypatch, user):
    monkeypatch.setattr('galpi.blueprints.root.me', lambda: user)


def test_get_all(monkeypatch, client, user):
    me(monkeypatch, user)
    client.put(f'/{user}/a', json={'link': 'a.com'}, ok=True)
    client.put(f'/{user}/b', json={'link': 'b.com'}, ok=True)

    # Both are vaild
    client.get(f'/{user}')
    client.get(f'/{user}/')
    assert client[-1].json == client.json == [
        {'user': user, 'path': 'a', 'link': 'a.com'},
        {'user': user, 'path': 'b', 'link': 'b.com'},
    ]


def test_put_item_overwrites(monkeypatch, client, user):
    me(monkeypatch, user)
    client.put(f'/{user}/a', json={'link': 'a.com'}, ok=True)
    client.put(f'/{user}/a', json={'link': 'a.org'}, ok=True)
    client.get(f'/{user}/a')
    assert client.json == {'user': user, 'path': 'a', 'link': 'a.org'}


def test_put_item_owner_only(monkeypatch, client, user):
    me(monkeypatch, None)
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    me(monkeypatch, 'NOT_OWNER')
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    me(monkeypatch, user)
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.CREATED
