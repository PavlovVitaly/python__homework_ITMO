code = 0
while code == 0:
    print('Введите три целых числа: ')
    input_string = input()
    input_string = input_string.split(' ')
    if len(input_string) != 3:
        print('Ошибка! Необходимо ввести три числа.')
        continue
    code = 1

list_of_input_val = list(map(int, input_string))

n = 1
while n < len(list_of_input_val):
    for i in range(len(list_of_input_val)-n):
        if list_of_input_val[i] > list_of_input_val[i+1]:
            list_of_input_val[i], list_of_input_val[i+1] = list_of_input_val[i+1], list_of_input_val[i]
    n += 1

output_string = list(map(str, list_of_input_val))
output_string = ', '.join(output_string)
print(output_string)