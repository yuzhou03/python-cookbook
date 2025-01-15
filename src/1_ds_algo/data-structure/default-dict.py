"""
defaultdict：带默认值的字典
功能：
当访问不存在的键时，自动为其生成一个默认值。
避免访问不存在的键时报错。
"""

from collections import defaultdict

# 创建 defaultdict
dd = defaultdict(list)
dd["a"].append(1)
dd["b"].append(2)
print(dd)  # 输出: defaultdict(<class 'list'>, {'a': [1], 'b': [2]})

# 未定义的键返回默认值
print(dd["c"])  # 输出: []
