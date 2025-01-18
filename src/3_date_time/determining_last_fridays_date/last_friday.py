from datetime import datetime, timedelta
from common.date import format_datetime
from common.seperator import delimiter

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print("today is ", format_datetime(datetime.now(), fmt="%Y-%m-%d"))
print("now is ", format_datetime(datetime.now()))
delimiter()

for day in weekdays:
    last_day = get_previous_byday(day)
    print(
        f"last {day:10} is {format_datetime(get_previous_byday(day), fmt='%Y-%m-%d')}"
    )
