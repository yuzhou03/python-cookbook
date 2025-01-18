from tabulate import tabulate
from common.text import print_pad


# 定义表格数据
data = [["Alice", 24], ["Bob", 27], ["Charlie", 22]]

# 打印表格
print_pad("grid style")
print(tabulate(data, headers=["Name", "Age"], tablefmt="grid"))
print_pad("simple style")
print(tabulate(data, headers=["Name", "Age"], tablefmt="simple"))

print_pad("grid style")
data = [
    {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "gender": "male",
    },
    {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles",
        "country": "USA",
        "gender": "male",
    },
    {
        "name": "Linda",
        "age": 35,
        "city": "Chicago",
        "country": "USA",
        "gender": "female",
    },
    {
        "name": "Mike",
        "age": 38,
        "city": "Beijing",
        "country": "China",
        "gender": "male",
    },
]
"""
tabulate(data, headers="keys", tablefmt="grid")：
data：这是一个包含字典的列表，每个字典代表一行数据。
headers="keys"：这个参数告诉 tabulate 使用字典的键作为表格的列标题。
tablefmt="grid"：这个参数指定了表格的格式为网格样式，即表格会有边框和分隔线。
"""
print(tabulate(data, headers="keys", tablefmt="grid"))
