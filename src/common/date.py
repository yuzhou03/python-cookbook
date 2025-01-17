from datetime import datetime


def format_datestr(date_str):
    # 将输入的时间字符串解析为 datetime 对象
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    # 返回格式化后的日期字符串
    return date_obj.strftime("%Y-%m-%d")


def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    # 使用 strftime 格式化 datetime 对象
    return dt.strftime(fmt)


def get_current_time():
    """
    获取当前时间并格式化为 YYYY-MM-DD HH:MM:SS
    """
    # 获取当前时间
    now = datetime.now()
    # 格式化为指定格式
    return now.strftime("%Y-%m-%d %H:%M:%S")


def __main__():
    print(get_current_time())
    print(format_datetime(datetime.now()))
    print(format_datetime(datetime.now(), "%Y-%m-%d"))
