#generator fubonacci
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))

# generator do czyania linia po lini
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

file_path = 'content.txt'
for line in read_large_file(file_path):
    print(line)

