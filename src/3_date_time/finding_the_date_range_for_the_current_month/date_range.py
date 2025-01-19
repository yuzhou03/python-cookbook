from datetime import datetime, date, timedelta
import calendar

from common.text import print_pad, delimiter


def get_month_range(start_date=None):
    """
    获取指定日期所在月份的起始日期和结束日期。

    参数:
    start_date (date, 可选): 指定的日期。如果未提供，则默认为当前日期。

    返回:
    tuple: 包含起始日期和结束日期的元组。
    """
    # 如果未提供 start_date，则将其设置为当前日期所在月份的第一天
    if start_date is None:
        start_date = date.today().replace(day=1)

    # 获取指定月份的天数
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]

    # 计算结束日期，即起始日期加上该月的天数
    end_date = start_date + timedelta(days=days_in_month)

    # 返回起始日期和结束日期的元组
    return start_date, end_date


if __name__ == "__main__":

    # Example usage
    start_date = date(2023, 1, 1)
    print_pad(f"Example usage: get_month_range(start_date={start_date})")
    first_day, last_day = get_month_range(start_date)

    a_day = timedelta(days=1)
    while first_day < last_day:
        print(first_day)
        first_day += a_day

    def date_range(start, stop, step):
        while start < stop:
            yield start
            start += step

    start_date = date(2012, 8, 1)
    end_date = date(2012, 8, 5)

    print_pad(f"date_range between {start_date} and {end_date}, step=timedelta(days=1)")

    for d in date_range(start_date, end_date, timedelta(days=1)):
        print(d)

    print_pad(
        f"date_range between {datetime(2012, 8, 1)} and {datetime(2012, 8, 2)}, step=timedelta(minutes=240)",
        size=100,
    )
    start_date = datetime(2012, 8, 1)
    end_date = datetime(2012, 8, 2)
    for d in date_range(start_date, end_date, timedelta(minutes=240)):
        print(d)
