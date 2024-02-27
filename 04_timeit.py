import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funcion '{func.__name__}' wykonana w : {end_time - start_time} seconds ")
        return result
    return wrapper

@timeit
def przykładowa_funkcja():
    time.sleep(1)

przykładowa_funkcja