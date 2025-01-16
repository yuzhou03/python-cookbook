import re
from common.seperator import delimiter

delimiter()
print("1. 基本匹配")
# 1. 基本匹配
# 匹配 "hello"
pattern = r"hello"
text = "hello world, hello python"

"""
re.search(pattern, text)：在 text 中搜索 pattern，返回第一个匹配的结果。
match.group()：返回匹配的字符串。
"""
match = re.search(pattern, text)

if match:
    print("Found:", match.group())  # 输出: Found: hello


# 2. 使用通配符
delimiter()
print("2. 使用通配符")
pattern = r"h.llo"  # "." 匹配任意单个字符
text = "hello world, hallo python"

matches = re.findall(pattern, text)  # re.findall(pattern, text)：返回所有匹配的结果。
print(matches)  # 输出: ['hello', 'hallo']


# 3. 匹配数字和字母
delimiter()
print("3. 匹配数字和字母")
pattern = r"\d+"  # "\d" 匹配数字, "+" 表示匹配一个或多个
text = "I have 2 apples and 10 bananas."

matches = re.findall(pattern, text)
print(matches)  # 输出: ['2', '10']

# 4. 匹配字符串开头和结尾
delimiter()
print("4. 匹配字符串开头和结尾")
pattern = r"^hello"  # "^" 匹配字符串开头
text = "hello world, hallo python"
if re.match(pattern, text):
    print("Starts with 'hello'")  # 输出: Starts with 'hello'

pattern = r"python$"  # "$" 表示匹配字符串的结尾
if re.search(pattern, text):
    print("Ends with 'python'")  # 输出: Ends with 'python'


"""
总结
\^：匹配字符串开头。
\$：匹配字符串结尾。
"""

# 5. 捕获组
delimiter()
print("5. 捕获组")
pattern = r"(\d+), (\d+)"
text = "Coordinates: 10, 20"
match = re.search(pattern, text)

print(match)  # <re.Match object; span=(13, 19), match='10, 20'>
if match:
    print("X:", match.group(1))  # 输出: X: 10
    print("Y:", match.group(2))  # 输出: Y: 20


# 6. 替换字符串
delimiter()
print("6. 替换字符串")
pattern = r"\d+"
text = "I have 2 apples and 10 bananas."

# re.sub(pattern, replacement, text)：用 replacement 替换匹配的 pattern。
result = re.sub(pattern, "X", text)
print(text)
print(result)  # 输出: I have X apples and X bananas.

# 7. 分割字符串
delimiter()
print("7. 分割字符串")
pattern = r"[,\s]+"  # 匹配逗号或空白字符
text = "apple,  banana  orange"
# re.split(pattern, text)：根据正则表达式匹配的内容分割字符串。
result = re.split(pattern, text)
print(text)
print(result)  # 输出: ['apple', 'banana', 'orange']


# 8. 贪婪匹配与非贪婪匹配
delimiter()
print("8. 贪婪匹配与非贪婪匹配")
text = "<html><head><title>Title</title></head></html>"
print(f"text: {text}")
# 贪婪匹配
pattern = r"<.*>"
match = re.search(pattern, text)
print(
    "Greedy match:", match.group()
)  # 输出: <html><head><title>Title</title></head></html>

# 非贪婪匹配
pattern = r"<.*?>"
match = re.search(pattern, text)
print("Non-greedy match:", match.group())  # 输出: <html>
"""
总结
*：贪婪匹配，尽可能多地匹配。
*?：非贪婪匹配，尽可能少地匹配。
"""

# 9. 编译正则表达式
delimiter()
print("9. 编译正则表达式")
# !编译正则表达式可以提高性能，尤其是在多次重复使用的情况下
pattern = re.compile(r"\d+")  # 编译正则表达式
print(f"pattern: {pattern}")
print("type(pattern)", type(pattern))
text = "There are 3 cats and 5 dogs."
print(f"text: {text}")
matches = pattern.findall(text)

print(matches)  # 输出: ['3', '5']


# 10. 忽略大小写匹配
delimiter()
print("10. 忽略大小写匹配")
pattern = r"hello"
print(f"pattern: {pattern}")
text = "Hello world"
print(f"text: {text}")
# re.IGNORECASE 或 re.I：忽略大小写。
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Matched(with ingnorecase option):", match.group())  # 输出: Matched: Hello
match = re.search(pattern, text)
if match:
    print("Matched:", match.group())  # 输出: Matched: Hello
else:
    print("No match")
