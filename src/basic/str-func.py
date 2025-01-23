from common.text import print_pad

"""
去除空白
str.strip()：去除首尾空白字符。
str.lstrip()：去除左侧空白。
str.rstrip()：去除右侧空白。
"""


def strip_demo():
    print_pad("strip_demo")
    s = "  Hello, World!  "
    print(s.strip(), len(s.strip()))  # "hello"
    print("s.rstrip() {len(s.rstrip())}")  # "  hello"
    print(s.lstrip(), len(s.lstrip()))  # "hello  "

    print(s.swapcase())  # hELLO, wORLD!


def string_find():
    """
    字符串查找
    str.find(sub, start=None, end=None)：查找子字符串 sub 在字符串中第一次出现的索引，找不到返回 -1。
    str.index(sub[, start[, end]])：同 find，但找不到会抛出异常。
    str.rfind(sub, start=None, end=None)：查找子字符串 sub 在字符串中最后一次出现的索引，找不到返回 -1。
    """

    s = "Hello, World!"
    print_pad("string_find")
    print(s)
    print("The index of 'World' in the string is:", s.find("World"))  # 7
    print("The index of 'Python' in the string is:", s.find("Python"))  # -1
    print("The last index of 'l' in the string is:", s.rfind("l"))  # 10
    print("The index of 'World' in the string is:", s.index("World"))  # 7

    try:
        print(s.index("Python"))  # ValueError: substring not found
    except ValueError as e:
        print(e)  # substring not found


def string_count():
    """
    字符串计数
    str.count(sub, start=None, end=None)：统计子字符串 sub 在字符串中出现的次数。
    """
    print_pad("string_count")
    s = "Hello, World!"
    print(s, 's.count("l")', s.count("l"))  # 3


def split_join():
    """
    字符串分割与连接

    该函数演示了如何使用 `split` 和 `join` 方法来处理字符串。
    `split` 方法用于将字符串分割成列表，`join` 方法用于将列表中的元素连接成字符串。
    """
    s = "apple,banana,orange"
    print_pad("split")
    print(s)
    print(s.split(","))  # ['apple', 'banana', 'orange']
    """
    使用 `split` 方法将字符串 `s` 按逗号分割成列表。
    输出结果为 ['apple', 'banana', 'orange']。
    """

    print_pad("join")
    fruits = ["apple", "banana", "orange"]
    print(fruits)
    print(", ".join(fruits))  # "apple, banana, orange"
    """
    使用 `join` 方法将列表 `fruits` 中的元素用逗号和空格连接成字符串。
    输出结果为 "apple, banana, orange"。
    """


def main():
    strip_demo()
    string_find()
    string_count()
    split_join()


if __name__ == "__main__":
    main()
