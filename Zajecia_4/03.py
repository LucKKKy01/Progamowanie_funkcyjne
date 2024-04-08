
data = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

def filter_even_values(a):
    return {key: value for key, value in a.items() if value % 2 == 0}

print(filter_even_values(data))  