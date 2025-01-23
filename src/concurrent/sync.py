# 多线程中共享数据可能导致竞争条件，需要使用同步机制。
import threading

# 使用 threading.Lock 来确保对共享变量 counter 的访问是线程安全的。
lock = threading.Lock()
counter = 0


def increment():
    global counter
    for _ in range(10000):
        # 确保在同一时刻只有一个线程能够执行 counter += 1，从而避免了竞争条件。
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()


print("Counter:", counter)

