from common.text import print_pad

# 方法签名
# str.split(sep=None, maxsplit=-1)
"""
参数说明
sep（可选）:

指定分隔符，类型为字符串。
如果为 None，则会以任意空白字符（空格、制表符、换行符等）为分隔符，并自动忽略开头和结尾的空白字符。
如果指定了 sep，相邻的多个分隔符不会被忽略（生成空字符串）。
maxsplit（可选）:

指定最多分割的次数，默认为 -1（不限制分割次数）。
如果指定了正整数，则分割最多发生 maxsplit 次，剩余部分将作为最后一个元素返回。
返回值
返回一个由分割后的子字符串组成的列表。
"""


def split_demo():
    # 示例 1: 以默认分隔符（空格）分割字符串
    print_pad("以默认分隔符（空格）分割字符串")
    text = "  Python is fun!  "
    result = text.split()
    print(result)  # 输出: ['Python', 'is', 'fun!']

    # 示例 2: 以逗号为分隔符，限制分割次数为 1
    print_pad("以逗号为分隔符，限制分割次数为 1")
    text = "apple,banana,orange"
    result = text.split(",", 1)
    print(result)  # 输出: ['apple', 'banana,orange']

    # 示例 3: 以空格为分隔符，不限制分割次数
    print_pad("以空格为分隔符，不限制分割次数")
    text = "Hello World"
    result = text.split(" ")
    print(text)
    print(result)  # 输出: ['Hello', 'World']

    # 示例 4: 以逗号为分隔符，不限制分割次数
    print_pad("以逗号为分隔符，不限制分割次数")
    text = "a,b,c,d,e"
    result = text.split(",", maxsplit=-1)
    print(text)
    print(result)  # 输出: ['a', 'b', 'c', 'd', 'e']


def split_sepcial_case():
    print_pad("split special cases")
    text = "hello   world"
    # 如果字符串中不存在指定的分隔符，split() 返回包含整个字符串的列表
    print_pad("如果字符串中不存在指定的分隔符，split() 返回包含整个字符串的列表")
    result = text.split(",")
    print(result)  # 输出: ['hello world']

    # 如果 sep 是 None，会忽略相邻的空白字符：
    print_pad("如果 sep 是 None，会忽略相邻的空白字符")
    result2 = text.split()
    print(result2)  # 输出: ['hello', 'world']

    # 如果字符串为空且 sep=None，返回一个空列表
    print_pad("如果字符串为空且 sep=None，返回一个空列表")
    text = ""
    result = text.split()
    print(result)

    # 如果字符串为空且指定 sep，返回包含一个空字符串的列表：
    print_pad("如果字符串为空且指定 sep，返回包含一个空字符串的列表")
    text = ""
    result = text.split(",")
    print(result)  # 输出: ['']


def split_csv_line():
    print_pad("split_csv_line")
    csv_line = "name,age,city"
    result = csv_line.split(",")
    print(csv_line)
    print(result)  # 输出: ['name', 'age', 'city']


def split_by_line():
    print_pad("split_by_line")
    text = "Line1\nLine2\nLine3"
    result = text.split("\n")
    print(text)
    print(result)  # 输出: ['Line1', 'Line2', 'Line3']


def main():
    split_demo()
    split_sepcial_case()
    split_csv_line()
    split_by_line()


if __name__ == "__main__":
    main()
