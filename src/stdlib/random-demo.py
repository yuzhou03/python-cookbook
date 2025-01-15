import random
from common.seperator import delimiter

max_attempt = 3

for i, _ in enumerate(range(max_attempt), start=1):
    print(f"第{i}次随机数：{random.random()}")
    # 生成一个随机浮点数
    #   0.0 <= random_float < 1.0
    random_float = random.random()
    print(f"第{i}次random_float: {random_float}")

    # 生成一个随机整数
    #   1 <= random_int <= 10
    random_int = random.randint(1, 10)
    print(f"第{i}次random_int: {random_int}")

    # 从序列中随机选择一个元素：
    my_list = ["Apple", "Vivo", "Oppo", "Huawei", "Xiaomi"]
    random_choice = random.choice(my_list)
    print(f"第{i}次random_choice: {random_choice}")
    delimiter()
