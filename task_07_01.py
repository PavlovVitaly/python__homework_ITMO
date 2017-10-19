def fibonacci(num):
    previous, current, n = 0, 1, num - 1
    yield previous
    yield current

    while n:
        previous, current, n = current, previous + current, n - 1
        yield current
