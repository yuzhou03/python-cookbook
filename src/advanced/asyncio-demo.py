import asyncio


async def fetch(url):
    print(f"Fetching {url}")
    # await 关键字用于等待异步操作完成
    await asyncio.sleep(1)  # 模拟网络请求
    return f"data from {url}"


# main 函数的作用是并发地执行多个异步任务（在这个例子中是模拟的网络请求），并打印出每个任务的结果。
# 并发执行任务的方式可以显著提高程序的效率，特别是在处理多个 I/O 密集型操作时。
async def main():
    # 创建三个任务并同时运行
    # 每个 fetch 函数调用都代表一个异步任务，用于模拟从不同 URL 获取数据的网络请求。
    tasks = [fetch("url1"), fetch("url2"), fetch("url3")]
    # 注意：这里使用了 asyncio.gather 来同时运行多个任务。
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
