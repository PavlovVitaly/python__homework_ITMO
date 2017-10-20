import collections
from inspect import signature


def __check_argument_types(types_of_var, sig):
    i = 0
    for key, value in sig.parameters.items():
        if not isinstance(types_of_var[i], value.annotation):
            raise TypeError('The argument "{}" must be "{}", passed "{}"'.format(key,
                                                                                 value.annotation,
                                                                                 type(types_of_var[i])))
        i += 1


def __check_not_iterable_return_type(result, sig):
    if not isinstance(result, sig.return_annotation):
        raise TypeError('The return value must be "{}", not "{}"'.format(sig.return_annotation,
                                                                         type(result)))
    else:
        return result


def __check_iterable_return_type(result, sig):
    i = 0
    for item in sig.return_annotation:
        if not isinstance(result[i], item):
            raise TypeError('The return value must be "{}", not "{}"'.format(item,
                                                                             type(result[i])))
        i += 1


def check_types(func):
    sig = signature(func)

    def wrapper(*args, **kwargs):
        types_of_var = args + tuple(kwargs.values())
        __check_argument_types(types_of_var, sig)

        result = func(*args, **kwargs)

        if not isinstance(sig.return_annotation, collections.Iterable):
            return __check_not_iterable_return_type(result, sig)

        __check_iterable_return_type(result, sig)

        return result

    return wrapper
