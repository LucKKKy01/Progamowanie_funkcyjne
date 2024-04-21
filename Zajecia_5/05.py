# zwraca parzyste liczy z lisy

numbers = [1,2,3,4,5,6]
result = []

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
        
even_numbers(numbers)


print(result)

# używa wyrażenia lambda do obliczneie pola prostokąta

area = lambda lenght, width : lenght * width
lenght = 2
width = 5

rectangle_area = area(lenght,width)
print(f'Pole = {rectangle_area}')