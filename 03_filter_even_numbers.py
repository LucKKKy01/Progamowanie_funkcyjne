def filter_even_numbers(numbers):
    return list(filter(lambda x: x%2 == 0, numbers))

print(filter_even_numbers([1,2,3,3,4,5]))