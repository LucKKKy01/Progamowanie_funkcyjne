from typing import Callable

def curry_add(a: int) -> Callable[[int], int]:
    def add_b(b: int) -> int:
        return a + b
    return add_b

add_5 = curry_add(5)
print(add_5(10)) # Output: 15