from http import HTTPStatus


def me(monkeypatch, user):
    monkeypatch.setattr('galpi.blueprints.root.me', lambda: user)


def preset(monkeypatch, user, client):
    me(monkeypatch, user)
    client.put(f'/{user}/a', ok=True)
    client.put(f'/{user}/a/1', json={'link': 'a1.com'}, ok=True)
    client.put(f'/{user}/a/2', json={'link': 'a2.com'}, ok=True)
    client.put(f'/{user}/b', json={'link': 'b.com'}, ok=True)


def test_get_all(monkeypatch, user, client):
    preset(monkeypatch, user, client)
    client.get(f'/{user}', ok=True)
    client.get(f'/{user}/', ok=True)
    assert client[-1].json == client.json == [
        {'user': user, 'path': 'a', 'link': None},
        {'user': user, 'path': 'a/1', 'link': 'a1.com'},
        {'user': user, 'path': 'a/2', 'link': 'a2.com'},
        {'user': user, 'path': 'b', 'link': 'b.com'},
    ]


def test_get_folder(monkeypatch, user, client):
    preset(monkeypatch, user, client)
    client.get(f'/{user}/a', ok=True)
    client.get(f'/{user}/a/', ok=True)
    assert client[-1].json == client.json == [
        {'user': user, 'path': 'a/1', 'link': 'a1.com'},
        {'user': user, 'path': 'a/2', 'link': 'a2.com'},
    ]


def test_get_link(monkeypatch, user, client):
    preset(monkeypatch, user, client)
    client.get(f'/{user}/b', ok=True)
    client.get(f'/{user}/b/', ok=True)
    assert client[-1].json == client.json == {
        'user': user,
        'path': 'b',
        'link': 'b.com'
    }


def test_put_item_only_within_folder(monkeypatch, user, client):
    preset(monkeypatch, user, client)
    client.put(f'/{user}/b/1')  # b is a link
    assert client.status == HTTPStatus.CONFLICT
    client.put(f'/{user}/c/1')  # c does not exist
    assert client.status == HTTPStatus.CONFLICT

    client.put(f'/{user}/x', ok=True)
    client.put(f'/{user}/x/y/z', json={'link': 'xyz.com'})
    assert client.status == HTTPStatus.CONFLICT

    client.put(f'/{user}/x/y', ok=True)
    client.put(f'/{user}/x/y/z', json={'link': 'xyz.com'}, ok=True)


def test_put_item_updates(monkeypatch, user, client):
    me(monkeypatch, user)

    # Create
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.CREATED
    assert client.headers['Content-Location'] == f'/{user}/a'
    client.get(f'/{user}/a')
    assert client.json == {'user': user, 'path': 'a', 'link': 'a.com'}

    # Update
    client.put(f'/{user}/a', json={'link': 'a.org'})
    assert client.status == HTTPStatus.NO_CONTENT
    assert client.headers['Content-Location'] == f'/{user}/a'
    client.get(f'/{user}/a')
    assert client.json == {'user': user, 'path': 'a', 'link': 'a.org'}

    # Updating a link as a folder is not allowed
    client.put(f'/{user}/a')
    assert client.status == HTTPStatus.CONFLICT

    # The opposite is also not allowed
    client.put(f'/{user}/b', ok=True)
    client.put(f'/{user}/b', json={'link': 'b.com'})
    assert client.status == HTTPStatus.CONFLICT


def test_put_item_owner_only(monkeypatch, user, client):
    me(monkeypatch, None)
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    me(monkeypatch, 'NOT_OWNER')
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.FORBIDDEN

    me(monkeypatch, user)
    client.put(f'/{user}/a', json={'link': 'a.com'})
    assert client.status == HTTPStatus.CREATED
