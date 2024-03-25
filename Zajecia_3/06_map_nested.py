def map_nested(lst, func):
    return [func(x) if isinstance(x, list) else x for x in lst]

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(map_nested(lst, lambda x: x * 2))