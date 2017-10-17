import time


def pause(delay_seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(delay_seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator
