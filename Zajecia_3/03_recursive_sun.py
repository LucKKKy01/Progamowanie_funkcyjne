numbers = [1,2,55,535,23,7]

def recursive_sum(numbers):
    if isinstance(numbers, list):
        return sum(numbers) + sum([recursive_sum(n) for n in numbers])
    else:
        return numbers
    
print(recursive_sum(numbers))