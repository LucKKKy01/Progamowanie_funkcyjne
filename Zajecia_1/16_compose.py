def compose(f, g):
    return lambda x: f(g(x))

from typing import Callable

def compose(f: Callable, g: Callable) -> Callable:
    def composed_function(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed_function

def add(a: int, b: int) -> int:
    return a + b

def mult(a: int, b: int) -> int:
    return a * b

composed_func = compose(add, mult)
print(composed_func(2, 3)) # Output: 10