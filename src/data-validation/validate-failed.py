from pydantic import BaseModel, ValidationError, validator
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime = None

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValidationError("Name must contain a space")
        return v.title()


# 有效的数据
valid_data = {"id": 1, "name": "john doe", "signup_ts": "2023-01-01T00:00:00"}

user = User(**valid_data)
print(user)

# 无效的数据
invalid_data = {
    "id": 2,
    "name": "janedoe",  # 缺少空格
    "signup_ts": "invalid_date",  # 无效的日期格式
}

try:
    user = User(**invalid_data)
except ValidationError as e:
    print(e.json())
