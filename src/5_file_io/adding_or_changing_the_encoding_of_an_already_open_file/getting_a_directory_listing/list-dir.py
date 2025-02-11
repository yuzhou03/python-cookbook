# Example of getting a directory listing

from datetime import datetime
import os
import os.path
import glob
from tabulate import tabulate

from common.text import print_pad, delimiter

# 获取所有以 .py 结尾的文件名
pyfiles = glob.glob("*.py")

# 获取文件大小和修改日期
name_sz_date = [
    (name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles
]

# 获取文件元数据
file_metadata = [(name, os.stat(name)) for name in pyfiles]

# 准备表格数据
table_data = []
for name, meta in file_metadata:
    last_modified_time = datetime.fromtimestamp(meta.st_mtime).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    table_data.append([name, meta.st_size, last_modified_time])

# 定义表格标题
print_pad("获取文件大小和修改日期，使用 tabulate 输出表格")
headers = ["文件名", "字节", "最后修改时间"]

# 使用 tabulate 输出表格, tablefmt="pipe" 表示使用竖线分隔列
print(tabulate(table_data, headers=headers, tablefmt="pipe"))


delimiter()
for r in name_sz_date:
    print(r)


print_pad("获取文件大小和修改日期")

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    last_modified_time = datetime.fromtimestamp(meta.st_mtime).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(
        f"文件名: {name}, 文件大小: {meta.st_size} Bytes, 最后修改时间: {last_modified_time}"
    )
