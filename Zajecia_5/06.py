# zaczynające się na litere a
my_words = ['kot', 'ala', 'zupa', 'arbuz']

def words_start_on_a(words_list):
    return list(filter(lambda word: word.lower().startswith('a'), words_list))

result = words_start_on_a(my_words)
print(f'Słowa na literę a : {result}')


# przekształcanie liczba na ich kwardary

numbers = [1,2,3,4,5]
def square_numbers(x):
    return x ** 2

maped_square_numbers = list(map(square_numbers, numbers))
print(maped_square_numbers)