import math

num = 16
# 求平方根
sqrt = math.sqrt(num)
print(f"sqrt of {num} is {sqrt}")

# 求绝对值
num = -10
abs_num = math.fabs(-10)
print(f"abs of {num} is {abs_num}")


# 计算三角函数值
angle = 45  # 角度
radian = math.radians(angle)
sin_result = math.sin(radian)
# 保留4位小数
print(f"sin_result of {angle} degree is {sin_result:.4f}")
