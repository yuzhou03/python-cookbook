# example.py
#
# Example of a regular expression that finds shortest matches

import re

from common.text import print_pad

# Sample text
text = 'Computer says "no." Phone says "yes."'

# (a) Regex that finds quoted strings - longest match
print_pad("longest match")
"""
代码中的正则表达式r"\"(.*)\""用于匹配双引号内的任意字符序列。这里的r表示原始字符串
\"匹配双引号
(.*) 是一个捕获组，匹配任意字符序列（除了换行符）。. 匹配除换行符以外的任意字符，* 表示匹配前面的子表达式零次或多次。
由于没有使用非贪婪模式（即没有在 * 后面加上 ?），这个正则表达式会尽可能多地匹配字符，直到遇到最后一个双引号。
"""
str_pat = re.compile(r"\"(.*)\"")
print("pattern", str_pat.pattern)

print("matches(greedy-mode)", str_pat.findall(text))  # ['no." Phone says "yes.']

# (b) Regex that finds quoted strings - shortest match
print_pad("shortest match")
"""
(.*?)匹配任意字符序列（除了换行符），并且使用了非贪婪模式（即最短匹配）。
"""
str_pat = re.compile(r"\"(.*?)\"")
print("pattern", str_pat.pattern)
print("matches(non-greedy mode)", str_pat.findall(text))  # ['no.', 'yes.']
