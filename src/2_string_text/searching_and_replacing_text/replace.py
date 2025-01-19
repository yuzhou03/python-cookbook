# example.py
#
# Examples of simple regular expression substitution

import re
from common.text import print_pad

# Some sample text
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
print_pad("Some sample text")
print(text)


datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# (a) Simple substitution
print_pad("Simple substitution")
print("replace date string. format: yyyy-mm-dd")
print(datepat.sub(r"\3-\1-\2", text))

# (b) Replacement function
from calendar import month_abbr


def change_date(m):
    # month_abbr: Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
    mon_name = month_abbr[int(m.group(1))]
    return "{} {} {}".format(m.group(2), mon_name, m.group(3))


print_pad("Replacement function")
print("replaced date string:", datepat.sub(change_date, text))


def show_month_abbr():
    """
    打印1到12月的英文缩写。

    该函数遍历从1到12的整数，并使用calendar模块中的month_abbr列表来打印每个月的英文缩写。
    """
    for i in range(1, 13):
        # 打印当前月份的数字和对应的英文缩写
        print(i, month_abbr[i])


show_month_abbr()
