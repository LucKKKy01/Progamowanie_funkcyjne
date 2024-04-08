from itertools import permutations

data = [1, 2, 3]

def generate_permutations(lst):
    return list(permutations(lst))


print(generate_permutations(data)) 