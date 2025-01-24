# 类装饰器：修改类的行为


# 通过类装饰器动态地向类中添加新的方法，从而修改类的行为。
# 应用场景：在运行时动态地修改类的属性或方法，实现一些特定的功能。
def add_method(cls):
    def new_method(self):
        print("New method added to the class")

    cls.new_method = new_method
    return cls


@add_method
class MyClass:
    def existing_method(self):
        print("Existing method in the class")


obj = MyClass()
obj.existing_method()  # 输出: Existing method in the class
obj.new_method()  # 输出: New method added to the class
