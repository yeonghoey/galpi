def test_foo(client):
    response = client.get('/yeonghoey', follow_redirects=True)
    print(response)
    assert False
