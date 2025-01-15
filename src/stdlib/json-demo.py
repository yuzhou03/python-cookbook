from common.seperator import delimiter
from common.file import read_file


# 将json字符串转成Python对象
import json

json_str = '{"name": "Alice", "age": 25, "city": "New York"}'
# 解析JSON字符串
data = json.loads(json_str)
# 访问数据
print(f"data: {data}")  # data: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(f"data type: {type(data)}")  # data type: <class 'dict'>
delimiter()

# 将 Python 对象写入 JSON 文件
data = {"name": "Alice", "age": 25, "city": "New York"}
file_path = "data.json"
with open(file_path, "w") as file:
    json.dump(data, file)
    print(f"写入文件{file_path}成功")

read_file(file_path)
delimiter()


# 从 JSON 文件读取数据并转换为 Python 对象
print("从 JSON 文件读取数据并转换为 Python 对象")
with open(file_path, "r") as f:
    restored_data = json.load(f)
print(f"restored_data: {restored_data}")
# 比较原始数据和恢复的数据内容是否相同
print(f"data == restored_data: {data == restored_data}")
