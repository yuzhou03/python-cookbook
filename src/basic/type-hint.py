from typing import List, Dict, Tuple, Set, Union
from typing import Any
from typing import Optional


from common.seperator import delimiter


# 列表
numbers: List[int] = [1, 2, 3]

# 字典
user_data: Dict[str, int] = {"Alice": 25, "Bob": 30}

# 元组
point: Tuple[int, int] = (10, 20)

# 集合
unique_ids: Set[int] = {1, 2, 3}

print("list", numbers)
print("dict", user_data)
print("tuple", point)
print("set", unique_ids)

delimiter()

# Any: 表示可以是任意类型
value: Any = "hello"
print("value of Any type", value)
value = 100  # 允许更改为其他类型
print("value of Any type", value)

delimiter()


# union: 表示可以是多种类型之一。
def process(value: Union[int, str]):
    return str(value)


print(process(100))
print(process("hello"))

delimiter()


# Optional表示可以是某种类型或 None。
def get_user_id(user: str):
    if user == "admin":
        return 1
    return None


print('get_user_id("admin")', get_user_id("admin"))
print('get_user_id("normal-user")', get_user_id("normal-user"))
