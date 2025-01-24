"""
元类（Metaclass）
功能：控制类的创建行为（类的“类”）。

应用场景：动态生成类、强制约束类属性、实现 ORM 框架。
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


a, b = Singleton(), Singleton()
print("a is b:", a is b)  # 输出: True
