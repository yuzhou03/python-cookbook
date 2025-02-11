# Reformulation using closures and function attributes
from functools import wraps


# 定义一个装饰器函数 profiled，用于统计函数的调用次数
def profiled(func):
    # 初始化调用次数为 0
    ncalls = 0

    @wraps(func)  # 使用 functools.wraps 保留原函数的元数据
    def wrapper(*args, **kwargs):
        # 使用 nonlocal 关键字声明 ncalls 为外部函数的变量
        nonlocal ncalls
        # 每次调用包装函数时，调用次数加 1
        ncalls += 1
        # 调用原函数并返回其结果
        return func(*args, **kwargs)
    # 为包装函数添加一个属性 ncalls，它是一个返回当前调用次数的函数
    wrapper.ncalls = lambda: ncalls
    # 返回包装函数
    return wrapper


# Example


@profiled
def add(x, y):
    return x + y


class Spam:
    @profiled
    def bar(self, x):
        print(self, x)


if __name__ == '__main__':
    print("add(2, 3)的计算结果:", add(2, 3))
    print("add(4, 5)的计算结果:", add(4, 5))
    print("add函数的调用次数:", add.ncalls())

    s = Spam()
    s.bar(1)
    s.bar(2)
    s.bar(3)
    print('ncalls:', Spam.bar.ncalls())
