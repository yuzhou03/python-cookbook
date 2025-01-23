"""
去除指定字符
str.removeprefix(prefix)：移除开头的指定前缀。
str.removesuffix(suffix)：移除结尾的指定后缀。
"""

s = "unhappy"
print(s.removeprefix("un"))  # "happy"
print(s.removesuffix("py"))  # "unhap"
