"""
multiprocessing 和 threading 是 Python 中实现并发编程的两种方式，但它们在实现机制、使用场景和性能上有显著区别。以下是它们的详细对比：

1. 概念
threading (多线程)

在同一个进程内创建多个线程，线程共享内存空间。
由于 Python 的 GIL（全局解释器锁）限制，线程不能真正并行执行 Python 字节码。
适用于 I/O 密集型任务。

multiprocessing (多进程)
使用独立的进程，每个进程有自己的内存空间。
没有 GIL 的限制，多个进程可以利用多核 CPU 实现真正的并行计算。
适用于 CPU 密集型任务。

2. 性能对比
特性	        threading	        multiprocessing
内存占用	    低（线程共享内存）	    高（每个进程独立内存空间）
上下文切换开销	 较低	               较高（进程切换开销大）
并行能力	    受 GIL 限制，伪并行	   真正并行
适用场景	    I/O 密集型任务	       CPU密集型任务


3. 使用场景
threading（适用于 I/O 密集型任务）：
文件读写。
网络请求（如爬虫、服务器并发处理）。



multiprocessing（适用于 CPU 密集型任务）：
大量计算（如矩阵运算、数据分析）。
图像处理。
机器学习模型训练。

"""

from multiprocessing import Process
import os


def cpu_heavy_task(name):
    print(f"Process {name} running on PID {os.getpid()}")
    result = sum(i**2 for i in range(10**6))
    print(f"Process {name} result: {result}")


if __name__ == "__main__":
    processes = [
        Process(target=cpu_heavy_task, args=(f"Process-{i}",)) for i in range(4)
    ]
    for p in processes:
        p.start()

    for p in processes:
        p.join()

"""
sample output
Process Process-3 running on PID 86289
Process Process-1 running on PID 86287
Process Process-0 running on PID 86286
Process Process-2 running on PID 86288
Process Process-3 result: 333332833333500000
Process Process-0 result: 333332833333500000
Process Process-2 result: 333332833333500000
Process Process-1 result: 333332833333500000
"""
