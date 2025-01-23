import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread {i}")


thread = MyThread()

# start 方法会在后台启动一个新线程，并调用 run 方法
thread.start()
# 阻塞当前线程，直到 thread 线程执行完毕。
thread.join()
