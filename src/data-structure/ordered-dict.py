"""
OrderedDict：有序字典
功能：
记住键值对的插入顺序(Python3.7及以上的普通字典默认也有此功能)。
在需要保留插入顺序的情况下使用。
"""

from collections import OrderedDict

# 普通dict
d = {}

d["b"] = 2
d["a"] = 1
d["c"] = 3
d["d"] = 4
print("普通dict", d)  # 输出: {'b': 2, 'a': 1, 'c': 3, 'd': 4}

# 创建 OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)  # 输出: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 键值对的插入顺序不会改变
od["d"] = 4
print(od)  # 输出: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
