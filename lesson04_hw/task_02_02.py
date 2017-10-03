def bubble_sort(lst):
    output_list = list(lst)
    n = 1
    while n < len(output_list):  # Сужаем неотсортированныю часть массива.
        for i in range(len(
                output_list) - n):  # Сравниваем соседние элементы в этом цикле. Самые большие значения будут "оседать" в конце массива.
            if output_list[i] > output_list[i + 1]:  # Если следующий элемент меньше текущего, то меняем их местами.
                output_list[i], output_list[i + 1] = output_list[i + 1], output_list[i]
        n += 1
    return output_list
