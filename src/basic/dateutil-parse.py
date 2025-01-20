from dateutil.parser import parse


def parse_date(date_str):
    # 解析 ISO 8601 格式的日期字符串
    date_str = "2023-10-15T12:30:00Z"
    date_obj = parse(date_str)
    print(date_obj)  # 输出: 2023-10-15 12:30:00+00:00

    # 解析 RFC 2822 格式的日期字符串
    date_str = "Sun, 15 Oct 2023 12:30:00 -0500"
    date_obj = parse(date_str)
    print(date_obj)  # 输出: 2023-10-15 12:30:00-05:00
