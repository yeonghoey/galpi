from galpi.db import users


def test_user(app_context, username):
    # Inserts
    users.upsert(username, 'http://example.com/a.jpg')
    assert users.get(username) == {
        'username': username,
        'avatar_url': 'http://example.com/a.jpg',
    }

    # Updates
    users.upsert(username, 'http://localhost/a.jpg')
    assert users.get(username) == {
        'username': username,
        'avatar_url': 'http://localhost/a.jpg',
    }
