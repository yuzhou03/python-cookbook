from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

# 计算两个日期之间的差值
date1 = parse("2023-10-15")
date2 = parse("2023-10-20")
delta = relativedelta(date2, date1)
print("date1", date1)
print("date2", date2)
print("days delta", delta.days)  # 输出: 5
