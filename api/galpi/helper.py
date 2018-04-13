def ensure_pathkey(pathquery):
    assert isinstance(pathquery, str)
    return pathquery.strip('/')
