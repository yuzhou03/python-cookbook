"""
带参数的装饰器
装饰器可以接受参数，用于修改其行为。
装饰器接受参数的方式是在装饰器函数内部再定义一个函数，用于接收参数。
"""


# 装饰器接受参数的示例：
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(5)  # 重复执行5次
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
