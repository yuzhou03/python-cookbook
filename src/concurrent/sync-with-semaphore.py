import threading
import time
from math import ceil

from common.text import delimiter, print_pad

print_pad("信号量semaphone")
# 创建一个信号量，初始值为3
SEMA_COUNT = 3
print("SEMA_COUNT", SEMA_COUNT)
semaphore = threading.Semaphore(SEMA_COUNT)  # 允许3个线程同时访问

# 记录程序开始时间
start_time = time.time()


# 模拟线程工作
def worker(thread_id):
    with semaphore:
        print(f"Thread {thread_id} is working")
        # 模拟工作
        threading.Event().wait(1)  # 当前线程暂停1秒
        print(f"Thread {thread_id} is done")


# 创建并启动6个线程
MAX_THREADS = 6
print("MAX_THREADS", MAX_THREADS)
delimiter()
threads = [threading.Thread(target=worker, args=(i,)) for i in range(MAX_THREADS)]

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

# 记录程序结束时间
end_time = time.time()

# 计算并输出程序执行时长
execution_time = end_time - start_time
# 这里的执行时间，是所有线程都完成工作的总时间，而不是单个线程的执行时间。大约等于 ceil(MAX_THREADS/SEMA_COUNT) 秒
# 因为在这个例子中，我们使用了一个信号量来限制同时访问的线程数量。当所有线程都在等待信号量时，程序会暂停，直到有线程释放信号量。
print(f"All threads are done. Execution time: {execution_time:.4f} seconds")

delimiter()


# 计算并输出程序预估执行时长
runtime_estimated = ceil(MAX_THREADS / SEMA_COUNT)
print("runtime estimated in seconds", runtime_estimated)
print(
    f"这里的执行时间，是所有线程都完成工作的总时间，而不是单个线程的执行时间。大约等于 ceil(MAX_THREADS/SEMA_COUNT) = {runtime_estimated} 秒"
)
