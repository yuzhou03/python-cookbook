"""
4. 数据共享
线程间共享内存：

线程共享全局变量，易发生 竞争条件，需要使用锁（threading.Lock）保护。
进程间独立内存：

进程间通过 multiprocessing.Queue 或 multiprocessing.Manager 实现数据通信，开销较大。
"""

from multiprocessing import Process, Manager


def increment(shared_dict, key):
    shared_dict[key] += 1


with Manager() as manager:
    shared_dict = manager.dict({"count": 0})
    processes = [
        Process(target=increment, args=(shared_dict, "count")) for _ in range(100)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(shared_dict["count"])  # 输出: 100
