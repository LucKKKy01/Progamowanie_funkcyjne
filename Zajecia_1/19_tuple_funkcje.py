def multiplytuple(input_tuple):
    modified_tuple = tuple(x + 1 for x in input_tuple)
    total_sum = sum(input_tuple)
    return modified_tuple, total_sum

my_tuple = (1, 2, 3, 4, 5)
result_tuple, total_sum = multiplytuple(my_tuple)

print('Orginal: ',my_tuple)

print('Modified: ',result_tuple)

print('Sum: ',total_sum)