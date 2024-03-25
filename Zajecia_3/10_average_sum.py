def cumulative_sum(numbers):
    cum_sum = []
    total = 0
    for num in numbers:
        total += num
        cum_sum.append(total)
    return cum_sum


numbers = [1, 2, 3, 4, 5]
print(cumulative_sum(numbers))