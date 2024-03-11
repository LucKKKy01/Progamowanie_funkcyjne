from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15]

def is_even(num):
    return num % 2 == 0

grouped = groupby(numbers, key=is_even)

for key, group in grouped:
    group_list  = list(group)
    print(f"{'Even' if key else 'Odd'} numbers: {group_list}")
    

    