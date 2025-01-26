# 利用 functools.lru_cache 缓存
from functools import lru_cache


# maxsize=None 缓存的大小将不受限制。这意味着所有的函数调用结果都将被缓存，直到程序结束
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))  # 快速计算结果 354224848179261915075
