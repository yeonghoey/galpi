from string import ascii_lowercase


def set_itemattrs(table, key, specs):
    assert len(specs) <= len(ascii_lowercase)

    exprs, attrs = [], {}
    for (path, value), ch in zip(specs, ascii_lowercase):
        exprs.append(f'SET {path} = :{ch}')
        attrs[f':{ch}'] = value

    return table.update_item(Key=key,
                             UpdateExpression=','.join(exprs),
                             ExpressionAttributeValues=attrs)
