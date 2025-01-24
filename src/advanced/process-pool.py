# 进程池加速 CPU 密集型任务

from multiprocessing import Pool
import math


# 判断一个数是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


from common.timer import timer_decorator


@timer_decorator
def main():
    with Pool(processes=4) as pool:
        # 使用进程池计算 1 到 1,000,000 之间的素数
        # 1_000_000 使用了下划线作为数字分隔符，这是Python 3.6及以上版本引入的特性，称为“数字字面量中的下划线”。这种写法的主要目的是提高代码的可读性，特别是对于大数字来说，更容易区分数字的位数。
        primes = pool.map(is_prime, range(1_000_000))
    print("Primes count:", sum(primes))  # Primes count: 78498


if __name__ == "__main__":
    main()
