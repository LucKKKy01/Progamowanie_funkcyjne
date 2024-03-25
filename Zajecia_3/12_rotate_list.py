def rotate_list(letters, steps):
    if not letters:
        return letters
    steps = steps % len(letters)
    return letters[-steps:] + letters[:-steps]

letters = ['a', 'b', 'c', 'd', 'e']
print(rotate_list(letters, 2))