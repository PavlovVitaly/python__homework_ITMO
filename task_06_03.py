from collections import namedtuple


def return_namedtuple(*elem_of_tuple):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, tuple):
                return result

            mock_result = namedtuple()
            # warning
            raise Exception

            return mock_result

        return wrapper

    return decorator
