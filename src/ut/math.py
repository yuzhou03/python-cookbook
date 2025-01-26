def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def power(x, y):
    return x**y


def sqrt(x):
    return x**0.5


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
