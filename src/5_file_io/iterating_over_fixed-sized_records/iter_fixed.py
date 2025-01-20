# Example of iterating of fixed-size records
#
# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.

# partial函数用于创建一个新的函数，该函数是原始函数的部分应用，即固定了原始函数的某些参数。
from functools import partial

RECORD_SIZE = 32

with open("data.bin", "rb") as f:
    # 这里的iter函数使用了一个偏函数partial，它将f.read作为原始函数，RECORD_SIZE作为固定参数。
    # 这样，每次调用新函数时，实际上是调用了f.read(RECORD_SIZE)，即每次读取RECORD_SIZE个字节。
    # 当f.read(RECORD_SIZE)返回空字节b''时，迭代器停止迭代。
    records = iter(partial(f.read, RECORD_SIZE), b"")
    for r in records:
        print(r)
