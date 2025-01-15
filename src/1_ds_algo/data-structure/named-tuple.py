from collections import namedtuple

# 定义一个 namedtuple
Point = namedtuple("Point", ["x", "y"])

# 创建实例
p = Point(10, 20)
print(p.x, p.y)  # 输出: 10 20
print(p[0], p[1])  # 也可以通过索引访问

# 转换为字典
print("转换为字典", p._asdict())  # 输出: {'x': 10, 'y': 20}
