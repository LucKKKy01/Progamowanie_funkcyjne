words = ["a", "a", "b", "c", "d", "e", "e"]

def remove_duplicates(words):
    return list(dict.fromkeys(words))

print(remove_duplicates(words))