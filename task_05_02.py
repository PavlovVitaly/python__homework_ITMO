def get_quadrant_number(x, y):
    if x * y == 0:
        raise ValueError

    if x > 0:
        if y > 0:
            return 1
        elif y < 0:
            return 4
    else:
        if y > 0:
            return 2
        elif y < 0:
            return 3
