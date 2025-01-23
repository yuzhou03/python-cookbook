import threading


def print_number():
    for i in range(1, 11):
        print(f"Number: {i}")


# 使用 threading.Thread 类创建线程
thread = threading.Thread(target=print_number)

# 启动线程
thread.start()

# 等待线程执行完毕
thread.join()
print("Main thread finished.")
