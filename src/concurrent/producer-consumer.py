import queue
import threading
from common.text import print_pad

q = queue.Queue()


def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")


def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed: {item}")
        q.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 这里的顺序确保生产者线程先完成，然后消费者线程再开始。
print_pad("producer")
producer_thread.start()
producer_thread.join()

print_pad("consumer")
consumer_thread.start()
consumer_thread.join()
