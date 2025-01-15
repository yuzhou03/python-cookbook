import queue
from common.seperator import delimiter

# 创建一个队列
q = queue.Queue(maxsize=3)
# 添加元素
q.put(1)
q.put(2)
q.put(3)

print("q.full()", q.full())
# 获取元素
print(q.get())  # Output: 1
print(q.get())  # Output: 2

print("q.empty()", q.empty())  # Output: False (队列不为空)

q.put(4)
print("q.put(4)")
print(q.get())  # Output: 3
print(q.get())  # Output: 4

delimiter()

# queue.LifoQueue 用法
print("LIFO Queue")
stack = queue.LifoQueue()

# 添加元素
stack.put(1)
stack.put(2)
stack.put(3)

# 获取元素（后进先出）
print(stack.get())  # Output: 3
print(stack.get())  # Output: 2
print(stack.get())  # Output: 1
delimiter()

# queue.PriorityQueue 用法
"""
PriorityQueue 是一个优先级队列，元素会按照优先级顺序出队（优先级值小的先出队）。
"""
print("Priority Queue")
# 创建优先级队列
pq = queue.PriorityQueue()

# 添加元素 (优先级, 元素)
pq.put((2, "middle priority"))
pq.put((1, "high priority"))
pq.put((3, "low priority"))
pq.put((4, "lowest priority"))

# 获取元素
while not pq.empty():  # empty() 返回 True 表示队列为空。
    print(pq.get())  # 获取队列中的元素
