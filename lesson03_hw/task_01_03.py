print('Введите три целых числа: ')
list_of_input_val = list()
for i in range(3):
    list_of_input_val.append(int(input()))

n = 1
while n < len(list_of_input_val):
    for i in range(len(list_of_input_val)-n):
        if list_of_input_val[i] > list_of_input_val[i+1]:
            list_of_input_val[i], list_of_input_val[i+1] = list_of_input_val[i+1], list_of_input_val[i]
    n += 1

output_string = list()
for i in list_of_input_val:
    output_string.append(str(i))
output_string = ', '.join(output_string)
print(output_string)