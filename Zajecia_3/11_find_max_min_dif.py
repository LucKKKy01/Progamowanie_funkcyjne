def find_max_min_diff(numbers):
    if not numbers:
        return None
    max_val = max(numbers)
    min_val = min(numbers)
    return max_val - min_val

numbers = [10, 5, 8, 3, 12]
print(find_max_min_diff(numbers))