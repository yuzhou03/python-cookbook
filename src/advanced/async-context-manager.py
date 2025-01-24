# 异步上下文管理器（Python 3.5+）


class AsyncContextManager:
    # 异步上下文管理器的进入方法
    async def __aenter__(self):
        # 当进入 async with 语句块时会被调用。在这个方法中，打印了 "Entering context"，并返回了 self，表示上下文管理器本身。
        print("Entering context")
        return self

    # 异步上下文管理器的退出方法
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 当退出 async with 语句块时会被调用。在这个方法中，打印了 "Exiting context"。
        print("Exiting context")


async def main():
    async with AsyncContextManager() as manager:
        print("Inside context")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
