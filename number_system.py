from functools import reduce

DICTIONARY_OF_NUMERATION_SYSTEM = {
    'bin': 2,
    'oct': 8,
    'hex': 16
}


def __convert_number_to_dec(number, from_num_sys):
    DICT = {ord('A'): '10',
            ord('B'): '11',
            ord('C'): '12',
            ord('D'): '13',
            ord('E'): '14',
            ord('F'): '15'}
    number = list(str(number).upper())
    number = list(map(lambda x: x.translate(DICT), number))
    number = list(map(int, number))
    number.reverse()
    number = list(map(lambda x, y: x * (from_num_sys ** y), number, range(len(number))))
    number = reduce(lambda x, y: x + y, number)
    return number


def __convert_number_from_dec(number, to_num_sys):
    remainder_list = list()
    while number > 0:
        remainder_list.append(number % to_num_sys)
        number //= to_num_sys
    DICT = {'10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'}
    remainder_list.reverse()
    remainder_list = list(map(str, remainder_list))
    find_in_dict_and_replace = lambda x: DICT[x] if x in DICT else x
    remainder_list = list(map(find_in_dict_and_replace, remainder_list))
    number = ''.join(remainder_list)
    return number


def dec2bin(number):
    return (lambda x: __convert_number_from_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['bin']))(number)


def dec2oct(number):
    return (lambda x: __convert_number_from_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['oct']))(number)


def dec2hex(number):
    return (lambda x: __convert_number_from_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['hex']))(number)


def bin2dec(number):
    return (lambda x: __convert_number_to_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['bin']))(number)


def oct2dec(number):
    return (lambda x: __convert_number_to_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['oct']))(number)


def hex2dec(number):
    return (lambda x: __convert_number_to_dec(x, DICTIONARY_OF_NUMERATION_SYSTEM['hex']))(number)
