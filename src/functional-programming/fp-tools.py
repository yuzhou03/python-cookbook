# Python的functools模块提供了一些高阶函数工具

"""
functools.partial
功能：固定函数的部分参数，生成一个新函数。
"""

from functools import partial


def add(a, b):
    return a + b


def partial_demo_1():

    # partial(add, 5)固定了add函数的第一个参数为5，生成了一个新函数add_5。
    add_5 = partial(add, 5)
    # 调用add_5(3)时，实际上是调用add(5, 3)，返回结果为8。
    print("add_5(3)", add_5(3))  # 输出: 8


def partial_demo_2():
    def power(base, exponent):
        return base**exponent

    square = partial(power, exponent=2)
    cube = partial(power, exponent=3)
    print("square(2)", square(2))  # 输出: 4
    print("cube(2)", cube(2))  # 输出: 8


# lru_cache 装饰器
# 功能：缓存函数的结果，避免重复计算。
def lru_cache_demo():
    from functools import lru_cache

    # lru_cache 装饰器可以缓存函数的结果，避免重复计算，从而提高函数的执行效率
    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("fibonacci(10)", fibonacci(10))  # 输出: 55


import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} 函数执行时间: {elapsed_time:.4f} 秒")
        return result

    return wrapper


@timer_decorator
def main():
    partial_demo_1()
    partial_demo_2()
    sleep_time = 1
    print(f"sleep {sleep_time}s")
    time.sleep(sleep_time)

    lru_cache_demo()


if __name__ == "__main__":
    main()
