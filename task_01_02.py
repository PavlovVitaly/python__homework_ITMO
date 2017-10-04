print('Введите количество тарелок: ')
number_of_palates = int(input())
print('Введите количество моющего средства (в ед.): ')
number_of_detergent = float(input())

current_number_of_palates = number_of_palates
current_number_of_detergent = number_of_detergent

while(current_number_of_palates > 0) and (current_number_of_detergent >= 0.5):
    current_number_of_palates -= 1
    current_number_of_detergent -= 0.5

if (current_number_of_palates > 0) and (current_number_of_detergent < 0.5):
    print('Моющее средство закончилось. Осталось', current_number_of_palates, 'тарелок')
elif (current_number_of_palates == 0) and (current_number_of_detergent >= 0.5):
    print('Все тарелки вымыты. Осталось', current_number_of_detergent, 'ед. моющего средства')
else:
    print('Все тарелки вымыты, моющее средство закончилось')
