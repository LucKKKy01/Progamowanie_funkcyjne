def custom_sort(my_list, key_func):
    return sorted(my_list, key=key_func)

my_list = ['jablko', 'banan', 'mango', 'marakuja']
sorted_list = custom_sort(my_list, key_func=len)
print("Posortowana lista:", sorted_list)