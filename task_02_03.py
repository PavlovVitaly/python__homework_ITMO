def average(lst):
    sum = 0
    for item in lst:
        sum += item
    avrg = sum / len(lst)
    return round(avrg, 3)
