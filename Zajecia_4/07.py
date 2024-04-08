
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'c': 4}

def merge_dictionaries(*dict):
    result = {}
    for d in dict:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

print(merge_dictionaries(dict1, dict2))  