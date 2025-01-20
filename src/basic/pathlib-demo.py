# pathlib 是python3.4 之后引入的标准库，主要是用来操作文件路径的

from pathlib import Path
from common.text import print_pad


# 遍历目录，递归列出木，类似于tree命令的功能
def tree(directory):
    print(f"+ {directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "    " * depth
        print(f"{spacer}+ {path.name}")


def show_path():
    # current path
    print_pad("current path")
    p = Path(".")
    print(p)
    print(p.absolute())

    # self defined path
    print_pad("self defined path")
    p = Path("/Users/why/Downloads")
    print(p.absolute())

    # absolute path
    print_pad("absolute path")
    home_path = Path.home()
    print(f"home_path: {home_path}")


def main():
    # 遍历目录
    print_pad("遍历目录")
    tree(Path("."))

    # 显示目录的路径
    print_pad("显示目录的路径")
    show_path()


if __name__ == "__main__":
    main()
