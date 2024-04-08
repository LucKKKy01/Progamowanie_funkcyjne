#Zmienne funkcyjne
def sum(a,b):
    return a + b

operation1 = sum
result = operation1(3,4)
print(result)

#Zmienne globalne
global_variable = 42

def print_global():
    print("Global variable value:", global_variable)

print_global()
