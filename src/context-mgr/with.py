from common.seperator import delimiter

"""
Python 上下文管理器 (with) 详解
上下文管理器是 Python 中用于管理资源的一种机制。它通过 with 语句简化了资源的获取和释放，确保资源能够在使用后正确清理（例如关闭文件、释放锁等）。以下是上下文管理器的详细解析：
"""

"""
基本语法
with expression as variable:
    # 使用资源的代码块
expression: 创建上下文管理器的对象（如打开文件）。
as variable: 可选部分，用于保存上下文管理器的返回值。
代码块: 在上下文管理器的管理下运行的代码。上下文退出时会自动清理资源。
"""

"""
2.1 文件操作
with 确保文件在使用后正确关闭，无论是否发生异常。
"""
with open("a.txt", "r") as file:
    content = file.read()
    print(content)
# 文件会在这里自动关闭

"""
2.2 数据库连接
"""
import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    conn.commit()
# 数据库连接自动关闭

"""
2.3 线程与锁
with 确保锁在使用后被释放。
"""
import threading

lock = threading.Lock()
with lock:
    # 临界区代码
    print("Critical section")
# 锁会在这里自动释放
delimiter()
"""
2.4 网络连接
"""

import requests

with requests.get("http://httpbin.org/get?name=John&age=30") as response:
    print("response.status_code", response.status_code)
    print(response.content)
# 连接会在这里自动关闭
