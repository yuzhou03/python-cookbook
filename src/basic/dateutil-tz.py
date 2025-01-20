from dateutil.parser import parse
from dateutil.tz import gettz

# 解析带有时区信息的日期字符串
date_str = "2023-10-15T12:30:00+08:00"  # 北京时区
date_obj = parse(date_str)
print(
    "date in Beijing timezone", date_obj
)  # 输出: date in Beijing timezone 2023-10-15 12:30:00+08:00

# 将日期转换为纽约时区
new_tz = gettz("America/New_York")
new_date_obj = date_obj.astimezone(new_tz)
print(
    "date in New York timezone", new_date_obj
)  # 输出: date in New York timezone 2023-10-15 00:30:00-04:00
