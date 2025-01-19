# example.py
#
# Example of using shell-wildcard style matching in list comprehensions


"""
fnmatch 是 Python 标准库中的一个模块，它提供了文件名匹配功能，使用的是 Unix shell 风格的通配符。这个模块在处理文件名或路径名时非常有用，特别是当你需要根据特定的模式来筛选文件或目录时。
文件名匹配：fnmatch 模块中的 fnmatch 和 fnmatchcase 函数可以用来检查文件名是否与给定的模式匹配。
"""
from fnmatch import fnmatchcase as match
from common.text import print_pad

addresses = [
    "5412 N CLARK ST",
    "1060 W ADDISON ST",
    "1039 W GRANVILLE AVE",
    "2122 N CLARK ST",
    "4802 N BROADWAY",
]
print_pad("addresses")
print(addresses)

patt1 = "* ST"
a = [addr for addr in addresses if match(addr, patt1)]
print_pad("patten: * ST")
print(a)


patt2 = "54[0-9][0-9] *CLARK*"
print_pad("patten: 54[0-9][0-9] *CLARK*")
b = [addr for addr in addresses if match(addr, patt2)]
print(b)
