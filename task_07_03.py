import collections
from inspect import signature


def strict_argument_types(func):
    sig = signature(func)

    def wrapper(*args, **kwargs) -> sig.return_annotation:
        types_of_var = args + tuple(kwargs.values())
        i = 0
        for key, value in sig.parameters.items():
            if not isinstance(types_of_var[i], value.annotation):
                raise TypeError('The argument "{}" must be "{}", passed "{}"'.format(key,
                                                                                     value.annotation,
                                                                                     type(types_of_var[i])))
            i += 1
        return func(*args, **kwargs)

    return wrapper


def strict_return_type(func):
    sig = signature(func)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        i = 0

        if not isinstance(sig.return_annotation, collections.Iterable):
            if not isinstance(result, sig.return_annotation):
                raise TypeError('The return value must be "{}", not "{}"'.format(sig.return_annotation,
                                                                                 type(result)))
            else:
                return result
            
        for item in sig.return_annotation:
            if not isinstance(result[i], item):
                raise TypeError('The return value must be "{}", not "{}"'.format(item,
                                                                                 type(result[i])))
            i += 1

        return result

    return wrapper
