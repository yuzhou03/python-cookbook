from datetime import datetime, timedelta

# 获取当前日期和时间
now = datetime.now()

# 计算一周后的日期
one_week_later = now + timedelta(weeks=1)
one_week_later2 = now + timedelta(days=7)

# 以上两种方式等价
print(one_week_later)
print(one_week_later2)
