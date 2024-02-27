def make_multiplitier(x):
    def multiplitier(n):
        return x * n
    return multiplitier

double = make_multiplitier(2)
print(double(5))