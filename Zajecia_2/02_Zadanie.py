from itertools import combinations

def all_combinations(element):
    return list(combinations(element, 2))

print(all_combinations([1,2,3]))
