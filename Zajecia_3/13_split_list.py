def split_list(numbers, chunk_size):
    return [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(split_list(numbers, 3))