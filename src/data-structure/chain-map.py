"""
ChainMap：字典的集合视图
功能：
支持快速在两端添加和删除元素。
已在上文详细介绍。
"""

from collections import ChainMap
from common.seperator import delimiter


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

cm = ChainMap(dict1, dict2)
print(cm)  # 输出: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# 查找按顺序进行
print("查找按顺序进行", cm["b"])  # 输出: 2（优先使用 dict1 的值）
delimiter()

# 更新某个字典
print("更新某个字典")
cm["c"] = 5
print(dict2)  # 输出: {'b': 3, 'c': 5}
