# 自定义上下文管理器

from contextlib import contextmanager

from common.text import print_pad


@contextmanager
def managed_file(filename):
    try:
        f = open(filename, "w")
        yield f
    finally:
        f.close()


def process(filename):
    with managed_file(filename) as f:
        f.write("Hello, World!\n")
        f.write("This is a managed file example, implemented by contextlib.\n")


def main():
    out_file = "contextlib-demo.txt"
    process(out_file)
    print(f"write file done. output to file: {out_file}")
    print_pad("file content")
    read_file(out_file)


def read_file(filename):
    with open(filename, "r") as f:
        content = f.read().rstrip()
        print(content)


if __name__ == "__main__":
    main()
