def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x+2, value=10)

print(result)