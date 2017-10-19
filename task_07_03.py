import os
from inspect import signature


def strict_argument_types(func):
    def wrapper(*args, **kwargs):
        sig = signature(func)
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
    def wrapper(*args, **kwargs):
        sig = signature(func)
        result = func(*args, **kwargs)
        i = 0

        for item in sig.return_annotation:
            if not isinstance(result[i], item):
                raise TypeError('The return value must be "{}", not "{}"'.format(item,
                                                                                 type(result[i])))
            i += 1

        return result

    return wrapper


# @strict_argument_types
# # @strict_return_type
# def summa(a:int, b:int) -> [int, float]:
#     return a + b
#
# try:
#     res = summa(1, 3)
#     print(res)
#
# except TypeError as e:
#     print(e)
#
#
# @strict_argument_types
# # @strict_return_type
# def summa(a:int, b:int) -> [int, float]:
#     return a + b
#
# try:
#     res = summa(a=1, b=3)
#     print(res)
#
# except TypeError as e:
#     print(e)
#
# try:
#     res = summa(1.2, 3)
#     print(res)
# except TypeError as e:
#     print(e)


# @strict_argument_types
@strict_return_type
def splitext(path: str) -> (str, str):
    filename, ext = os.path.splitext(path)
    # return filename, ext.strip('.').lower()
    return ('sdsdsd', (2.2))


try:
    res = splitext('D:\Project\Stady_Prj\Python\python__homework_ITMO\task_07_03.py')
    print(res)
except TypeError as e:
    print(e)
