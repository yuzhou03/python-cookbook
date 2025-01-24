# 锁是最简单的同步机制，它可以确保同一时刻只有一个线程可以访问共享资源。
import threading

# 共享资源
counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        # lock.acquire() 方法用于获取锁，如果锁已经被其他线程获取，则当前线程会被阻塞，直到锁被释放。
        lock.acquire()
        counter += 1
        # lock.release() 方法用于释放锁，允许其他线程获取锁并访问共享资源。
        lock.release()


# 创建线程
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
