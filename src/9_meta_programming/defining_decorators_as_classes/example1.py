# Example of defining a decorator as a class
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
        self.ncalls = 0

    """
    每次调用该函数，__call__ 方法会被触发，从而更新调用次数计数器 ncalls，并执行原始函数。
    """

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# Example

@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


if __name__ == "__main__":
    print("add(2, 3)的结果:", add(2, 3))
    print("add(4, 5)的结果:", add(4, 5))
    print("add函数调用次数ncalls:", add.ncalls)

    print()

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print('ncalls:', Spam.bar.ncalls)
