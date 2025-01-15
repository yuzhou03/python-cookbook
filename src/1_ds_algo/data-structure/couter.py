from collections import Counter
from common.seperator import delimiter

"""
功能：
用于统计可迭代对象中元素的个数。
返回一个类似字典的对象，键是元素，值是计数。
"""

# 创建 Counter 对象
string = "abracadabra"
c = Counter(string)
print(string)
print(c)  # 输出: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 获取元素计数
print('c["a"]', c["a"])  # 输出: 5
print('c["z"]', c["z"])  # 不存在的键返回 0

delimiter()


# 更新计数
print("更新计数")
c.update("aaa")
print(c)  # 输出: Counter({'a': 8, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 获取最常见的元素
print(c.most_common(2))  # 输出: [('a', 8), ('b', 2)]
