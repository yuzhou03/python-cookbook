from common.seperator import delimiter

# 匿名函数，通常用于简单的逻辑。
add = lambda x, y: x + y
print("add(1, 2)", add(1, 2))  # 输出: 3

# 在高阶函数中使用：
nums = [1, 2, 3, 4, 5]
incremented = map(lambda x: x + 1, nums)
print("nums", nums)
print("incremented", list(incremented))  # 输出: [2, 3, 4, 5, 6]


# 不可变数据
delimiter()
nums = (1, 2, 3)
new_nums = tuple(map(lambda x: x * 2, nums))
print("nums", nums)  # Output: (1, 2, 3)
print("nums", new_nums)  # Output: (2, 4, 6)
