def fibonacci(num):
    previous, current, n = 0, 1, num - 1
    yield previous
    yield current

    while n:
        previous, current, n = current, previous + current, n - 1
        yield current


f = fibonacci(5)
print((fibonacci(5)))
print((fibonacci(5)))
print(next(fibonacci(5)))
print(next(fibonacci(5)))
print(next(fibonacci(5)))
print(next(fibonacci(5)))
