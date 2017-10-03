def bubble_sort(lst):
    output_list = list(lst)
    n = 1
    while n < len(output_list):
        for i in range(len(output_list) - n):
            if output_list[i] > output_list[i + 1]:
                output_list[i], output_list[i + 1] = output_list[i + 1], output_list[i]
        n += 1
    return output_list
