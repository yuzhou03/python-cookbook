"""
自定义上下文管理器
要自定义上下文管理器，需要实现以下两个方法：

__enter__(): 在进入上下文时执行，返回资源对象（可选）。
__exit__(exc_type, exc_value, traceback): 在退出上下文时执行，用于清理资源。
"""


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# 使用自定义上下文管理器
filename = "example.txt"
content = "Hello, world!\n"
with FileManager(filename, "w") as file:
    file.write(content)  # 文件写入操作, truncate file

# 文件自动关闭
with open(filename, "r") as file:
    print(file.read())
