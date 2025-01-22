from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from common.text import print_pad

"""
在Pydantic中，如果一个字段没有默认值，那么它就是必填的。这意味着在创建User实例时，必须提供一个值给id字段，否则Pydantic会抛出一个验证错误。
"""


class User(BaseModel):
    id: int  # 必填字段
    name: str = "John Doe"  # 可选字段, 默认为 "John Doe"
    signup_ts: Optional[datetime] = None  # 可选字段, 默认为 None
    friends: list[int] = []  # 可选字段, 默认为空列表


external_data = {
    "id": "123",  #! 如果没有设置id, 则会抛出验证错误
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)

print_pad("validate user")
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print("User ID:", user.id)

# > 123
