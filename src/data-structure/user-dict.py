from collections import UserDict
from common.text import print_pad


class MyDict(UserDict):
    def __missing__(self, key):
        """
        当访问的键不存在时调用此方法。

        参数:
            key: 访问的键。

        返回:
            一个默认值，这里返回0。
        """
        print(f"__missing__({key})")
        return 0

    def __setitem__(self, key, value):
        """
        当设置键值对时调用此方法。

        参数:
            key: 要设置的键。
            value: 要设置的值。
        """
        print(f"Setting ({key} = {value})")
        super().__setitem__(key, value)


d = MyDict()
print_pad("set key")
d["id"] = 1
print(d)
print_pad("access not exist key")
print(d["not_exist"])
