# Example of unwrapping a decorator

from functools import wraps
from common.text import print_pad


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


# Calling wrapped function
print_pad('Calling wrapped function')
print(add(2, 3))


# Calling original function
print_pad('Calling original function. The original function is the one that is wrapped by the innermost decorator', size=120)
print(add.__wrapped__(2, 3))


print_pad(
    'Calling the original function of the original function. with twice __wrapped__', size=120)
print(add.__wrapped__.__wrapped__(2, 3))
