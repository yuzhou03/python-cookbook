# 根据条件筛选元素。
nums = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # 输出: [2, 4]
