from common.seperator import delimiter

# Python 提供了 contextlib 模块来简化上下文管理器的创建。
"""
4.1 使用 @contextmanager
通过装饰器将普通函数转换为上下文管理器。
"""

from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


# 使用上下文管理器
content = "Hello, world!\n"
with open_file("test.txt", "w") as f:
    f.write(content)

with open_file("test.txt", "r") as f:
    print(f.read())  # 输出: Hello, world!

delimiter()

"""
4.2 忽略特定异常
contextlib.suppress 用于忽略指定异常。
"""
from contextlib import suppress

# 不会抛出异常
with suppress(ZeroDivisionError):
    print(10 / 0)

# 不会抛出异常
with suppress(FileNotFoundError):
    with open("nonexistent.txt", "r") as f:
        print(f.read())


"""
4.3 嵌套上下文
contextlib.ExitStack 管理多个上下文。
"""
from contextlib import ExitStack

with ExitStack() as stack:
    file1 = stack.enter_context(open("file1.txt", "w"))
    file2 = stack.enter_context(open("file2.txt", "w"))
    # 在这里可以同时使用 file1 和 file2
    file1.write("Hello")
    file2.write("World")
# 所有文件会在离开 with 块时自动关闭

"""
5. 优势与注意事项
5.1 优势
自动资源管理: 无需手动清理资源。
简洁清晰: 代码更简洁，逻辑更清晰。
异常安全: 即使发生异常，也能正确释放资源。
5.2 注意事项
上下文管理器的范围: 在 with 代码块外，资源不再可用。
性能: 对性能影响通常较小，但大量嵌套可能增加复杂性。
正确实现 __exit__: 必须处理异常参数，防止意外吞掉异常。
"""
