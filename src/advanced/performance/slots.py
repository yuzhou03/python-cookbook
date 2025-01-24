import sys
from common.text import print_pad
from pympler import asizeof


class RegularClassMulti:
    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j


class SlotsClassMulti:
    __slots__ = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

    def __init__(self, a, b, c, d, e, f, g, h, i, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j


# 创建 RegularClassMulti 和 SlotsClassMulti 的实例
regular_instance = RegularClassMulti(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slot_instance = SlotsClassMulti(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print_pad("多属性测试(sys.getsizeof)")

# 打印类的内存占用
print(
    "RegularClassMulti:",
    sys.getsizeof(RegularClassMulti(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
)  # 可能输出 152
print(
    "SlotsClassMulti:  ", sys.getsizeof(SlotsClassMulti(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
)  # 可能输出 120

# 打印实例的内存占用
# sys.getsizeof()函数返回的是对象本身的内存占用，而不包括__slots__中定义的属性的内存占用。
# 因此，在使用__slots__时，sys.getsizeof()函数返回的结果可能会比使用普通类时要小。
print_pad("多属性测试(asizeof.asizeof)")
# asizeof函数会递归地计算对象及其引用的所有对象的内存占用
print("RegularClassMulti size:", asizeof.asizeof(regular_instance))
print("SlotsClassMulti size:", asizeof.asizeof(slot_instance))


"""
------------------------------多属性测试(sys.getsizeof)------------------------------
RegularClassMulti: 48
SlotsClassMulti:   112
-----------------------------多属性测试(asizeof.asizeof)-----------------------------
RegularClassMulti size: 1136
SlotsClassMulti size: 432
"""
