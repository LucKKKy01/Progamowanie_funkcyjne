def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper

@safe_function
def calculate_factorial(a, b):
    return a / b

print(calculate_factorial(2, 0))