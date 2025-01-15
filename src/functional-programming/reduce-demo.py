nums = [1, 2, 3, 4, 5]

# 使用 reduce 计算列表中所有元素的和
from functools import reduce

sum = reduce(lambda x, y: x + y, nums)
print("reduce result(sum)", sum)  # 输出: 15

product = reduce(lambda x, y: x * y, nums)
print("reduce result(product)", product)  # 输出: 120
