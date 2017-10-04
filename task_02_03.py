from functools import reduce

def average(lst):
    avrg = reduce(lambda x, y: x + y, lst) / len(lst)
    return round(avrg, 3)
