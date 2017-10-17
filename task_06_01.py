import platform


def __is_mac():
    if platform.system() is 'Darwin':
        return True
    return False


def __is_windows():
    if platform.system() is 'Windows':
        return True
    return False


def __is_linux():
    if platform.system() is 'Linux':
        return True
    return False


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
