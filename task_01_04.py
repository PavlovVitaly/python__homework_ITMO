NUMBER_OF_COORDINATE = 6
COORD_OF_VERTEX = {'a_x': 0,
                   'a_y': 1,
                   'b_x': 2,
                   'b_y': 3,
                   'c_x': 4,
                   'c_y': 5}

LENGTH_OF_SIDES = {'a': 0,
                   'b': 1,
                   'c': 2}

list_of_coord = list()
for i in range(NUMBER_OF_COORDINATE):
    list_of_coord.append(int(input()))

# 2 7 6 1 12 5
length_of_sides = list()
length_of_sides.append(((list_of_coord[COORD_OF_VERTEX['b_x']] - list_of_coord[COORD_OF_VERTEX['a_x']]) ** 2) +
                       ((list_of_coord[COORD_OF_VERTEX['b_y']] - list_of_coord[COORD_OF_VERTEX['a_y']]) ** 2))
length_of_sides.append(((list_of_coord[COORD_OF_VERTEX['c_x']] - list_of_coord[COORD_OF_VERTEX['b_x']]) ** 2) +
                       ((list_of_coord[COORD_OF_VERTEX['c_y']] - list_of_coord[COORD_OF_VERTEX['b_y']]) ** 2))
length_of_sides.append(((list_of_coord[COORD_OF_VERTEX['a_x']] - list_of_coord[COORD_OF_VERTEX['c_x']]) ** 2) +
                       ((list_of_coord[COORD_OF_VERTEX['a_y']] - list_of_coord[COORD_OF_VERTEX['c_y']]) ** 2))

if (length_of_sides[LENGTH_OF_SIDES['a']] == length_of_sides[LENGTH_OF_SIDES['b']] + length_of_sides[
    LENGTH_OF_SIDES['c']]) or \
        (length_of_sides[LENGTH_OF_SIDES['b']] == length_of_sides[LENGTH_OF_SIDES['a']] + length_of_sides[
            LENGTH_OF_SIDES['c']]) or \
        (length_of_sides[LENGTH_OF_SIDES['c']] == length_of_sides[LENGTH_OF_SIDES['a']] + length_of_sides[
            LENGTH_OF_SIDES['b']]):
    print('Прямоугольный')
else:
    print('Не прямоугольный')
