# 对可迭代对象的每个元素应用函数，返回迭代器。
nums = [1, 2, 3, 4, 5]
sequared = map(lambda x: x**2, nums)
print(list(sequared))  # [1, 4, 9, 16, 25]
