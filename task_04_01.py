n = int(input())
p = int(input())
with open('data.txt') as input_file:
    content = str(input_file.read())

content = list(content.split(' '))
content = list(map(int, content))
content_of_out_file_1 = list(filter(lambda x: (x % n) == 0, content))
content_of_out_file_1 = list(map(str, content_of_out_file_1))
content_of_out_file_1 = ' '.join(content_of_out_file_1)

with open('out-1.txt', 'w') as out_file_1:
    out_file_1.write(content_of_out_file_1)

content_of_out_file_2 = list(map(lambda x: x ** p, content))
content_of_out_file_2 = list(map(str, content_of_out_file_2))
content_of_out_file_2 = ' '.join(content_of_out_file_2)

with open('out-2.txt', 'w') as out_file_2:
    out_file_2.write(content_of_out_file_2)
