def __is_mac():
    pass


def __is_windows():
    pass


def __is_linux():
    pass


def run_on_linux(func):
    if not __is_linux():
        return None

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def run_on_macos(func):
    if not __is_mac():
        return None

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def run_on_windows(func):
    if not __is_windows():
        return None

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
