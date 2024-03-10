from functools import partial

def multiply(x, y):
    return x * y

add_five = partial(multiply, 5)

result = add_five(10)

print(result) # Output: 25