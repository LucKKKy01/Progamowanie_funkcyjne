from itertools import product

list1 = ['A', 'B']
list2 = ['C', 'D']

all_combines = list(product(list1, list2))

for combination in all_combines:
    print(combination)