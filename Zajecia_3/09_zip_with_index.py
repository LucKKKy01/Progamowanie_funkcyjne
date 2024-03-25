lst = ['a', 'b', 'c', 'd']

def zip_with_index(lst):
    return list(enumerate(lst))

zipped = zip_with_index(lst)
print(zipped)