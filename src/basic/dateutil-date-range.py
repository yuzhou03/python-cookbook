from dateutil.rrule import rrule, DAILY
from datetime import datetime

from common.text import print_pad

# 生成从 2023-10-15 到 2023-10-20 的日期序列
start_date = datetime(2023, 10, 15)
end_date = datetime(2023, 10, 20)
print_pad(f"calculate date range using rrule DAILY from dateutil library")
print_pad(
    f"start date: {start_date.strftime('%Y-%m-%d')}, end date: {end_date.strftime('%Y-%m-%d')}"
)

dates = list(rrule(DAILY, dtstart=start_date, until=end_date))
"""
输出: 
[
    datetime.datetime(2023, 10, 15, 0, 0), 
    datetime.datetime(2023, 10, 16, 0, 0), 
    datetime.datetime(2023, 10, 17, 0, 0), 
    datetime.datetime(2023, 10, 18, 0, 0), 
    datetime.datetime(2023, 10, 19, 0, 0), 
    datetime.datetime(2023, 10, 20, 0, 0),
]
"""
print(dates)
print_pad("date range")
for dt in dates:
    # 将dt格式化为字符串，输出格式为"2023-10-15"
    print(dt.strftime("%Y-%m-%d"))
