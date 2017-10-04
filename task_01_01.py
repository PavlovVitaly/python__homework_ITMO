# CONST
LENGTH_OF_SEEDBED_IN_METERS = 15
WIDTH_OF_SEEDBED_IN_METERS = 25
COEFFICIENT_SOTKI_TO_SQUARE_METERS = 100
AREA_OF_SEEDBED_IN_SQUARE_METERS = LENGTH_OF_SEEDBED_IN_METERS * WIDTH_OF_SEEDBED_IN_METERS
# END CONST

area_square_meters = int(float(input()) * COEFFICIENT_SOTKI_TO_SQUARE_METERS)

if area_square_meters >= 0:
    free_area_in_square_meters = area_square_meters % AREA_OF_SEEDBED_IN_SQUARE_METERS
    print(free_area_in_square_meters)
else:
    print(0)
