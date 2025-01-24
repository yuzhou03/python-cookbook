# 装饰器是高阶函数的一个应用。
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@decorator
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
# Output:
# Before function call
# Hello, Alice
# After function call
