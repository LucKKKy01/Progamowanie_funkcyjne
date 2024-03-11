def even_numbers():
    number = 0
    while True:
        number += 1

generator = even_numbers()

for _ in range(10):
    print(next(generator))