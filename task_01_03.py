NUMBER_OF_NUMBERS = 3
list_of_input_val = list()
for i in range(NUMBER_OF_NUMBERS):
    list_of_input_val.append(int(input()))

n = 1
while n < len(list_of_input_val):
    for i in range(len(list_of_input_val)-n):
        if list_of_input_val[i] > list_of_input_val[i+1]:
            list_of_input_val[i], list_of_input_val[i+1] = list_of_input_val[i+1], list_of_input_val[i]
    n += 1

output_string = list(map(str, list_of_input_val))
output_string = ', '.join(output_string)
print(output_string)
