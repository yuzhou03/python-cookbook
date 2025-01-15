from collections import deque
from common.seperator import delimiter

print("DEQUEUE usage demo")
print("deque 是一个高效、灵活的数据结构，非常适合频繁操作队列两端的场景。")
delimiter()
# 创建一个空的 deque
dq = deque()

# 创建一个带初始元素的 deque
dq = deque([1, 2, 3, 4])
print(dq)  # 输出: deque([1, 2, 3, 4])

delimiter()

# 添加元素
"""
append()：在右端添加元素。
appendleft()：在左端添加元素。
"""
dq = deque([1, 2, 3])
dq.append(4)  # 右端添加 4
dq.appendleft(0)  # 左端添加 0
print(dq)  # 输出: deque([0, 1, 2, 3, 4])
delimiter()


# 删除元素
"""
pop()：从右端移除元素。
popleft()：从左端移除元素。
"""
dq = deque([0, 1, 2, 3, 4])
dq.pop()  # 移除右端的元素
dq.popleft()  # 移除左端的元素
print(dq)  # 输出: deque([1, 2, 3])
delimiter()


# 限制长度
# deque 支持设置最大长度 (maxlen)，当队列长度超过最大值时，旧元素会被自动移除。
print("限制长度")
dq = deque(maxlen=3)  # 最多只能容纳 3 个元素
dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)  # 添加 4 时，最左边的 1 被移除
print(dq)  # 输出: deque([2, 3, 4], maxlen=3)
delimiter()

# 其他操作
"""
extend() 和 extendleft()
extend() 在右端批量添加元素。
extendleft() 在左端批量添加元素（逆序插入）。
"""
dq = deque([1, 2])
dq.extend([3, 4])  # 在右端添加
dq.extendleft([0, -1])  # 在左端 逆序 添加
print(dq)  # 输出: deque([-1, 0, 1, 2, 3, 4])

delimiter()

"""
rotate(n)
队列中的元素向右旋转n次; n为负数时, 向左旋转。
"""
print("rotate(n):队列中的元素向右旋转n次; n为负数时, 向左旋转。")
dq = deque([1, 2, 3, 4, 5])
print(dq)  # 输出: deque([1, 2, 3, 4, 5])
dq.rotate(2)  # 向右旋转 2 次
print(dq)  # 输出: deque([4, 5, 1, 2, 3])
dq.rotate(-1)  # 向左旋转 1 次
print(dq)  # 输出: deque([5, 1, 2, 3, 4])
delimiter()


# clear()：清空队列
print("clear()：清空队列")
dq = deque([1, 2, 3])
dq.clear()
print(dq)  # 输出: deque([])
delimiter()

# count(x)：统计元素 x 在队列中出现的次数。
print("统计元素 x 在队列中出现的次数")
dq = deque([1, 2, 2, 3, 2, 1])
print("dq.count(2)", dq.count(2))  # 输出: 3
print("dq.count(1)", dq.count(1))  # 输出: 2
delimiter()
