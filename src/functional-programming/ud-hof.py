# 自定义高阶函数
from math import pow
from common.text import print_pad


# 接受函数作为参数
print_pad("接受函数作为参数")


def apply_function(func, *args):
    return func(*args)


result = apply_function(lambda x, y: x + y, 3, 4)
print(
    "apply_function(lambda x, y: x + y, 3, 4): ", result
)  # 输出: 7 这是因为 3 + 4 = 7

result = apply_function(pow, 5, 2)
print("apply_function(pow, 5, 2): ", result)  # 输出: 25.0 这是因为 5 的平方是 25

result = apply_function(lambda x: x**2, 5)
print("apply_function(lambda x: x**2, 5): ", result)  # 输出: 25 这是因为 5 的平方是 25


# 返回函数作为结果
print_pad("返回函数作为结果")


def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)
print("double(5) = ", double(5))  # 输出: 10
print("triple(5) = ", triple(5))  # 输出: 15


# 组合函数
print_pad("组合函数")


def compose(f, g):
    def composed(x):
        return f(g(x))

    return composed


add_one = lambda x: x + 1
square = lambda x: x**2
composed_func = compose(add_one, square)
print(
    "composed_func(3) = add_one(square(3)) = ", composed_func(3)
)  # 输出: 10 (先平方，再加1)
