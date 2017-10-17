from collections import namedtuple


def __is_same_dimension(tuple1, tuple2):
    return len(tuple1) == len(tuple2)


def correct_dimension_of_tuple(tuple1, tuple2):
    dim = __get_less_dimension(tuple1, tuple2)
    return tuple1[:dim], tuple2[:dim]


def __get_less_dimension(tuple1, tuple2):
    if len(tuple1) > len(tuple2):
        return len(tuple2)
    return len(tuple1)


def return_namedtuple(*elem_of_tuple):
    def decorator(func):
        def wrapper(*args, **kwargs):
            temp_elem_of_tuple = elem_of_tuple[:]
            result = func(*args, **kwargs)

            if not isinstance(result, tuple):
                return result

            if not __is_same_dimension(temp_elem_of_tuple, result):
                temp_elem_of_tuple, result = correct_dimension_of_tuple(temp_elem_of_tuple, result)

            NamedTuple = namedtuple('NamedTuple', temp_elem_of_tuple)
            mock_result = NamedTuple._make(result)
            return mock_result
        return wrapper
    return decorator
