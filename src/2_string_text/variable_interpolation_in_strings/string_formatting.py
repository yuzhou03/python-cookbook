# example.py
#
# Examples of variable interpolation


# Class for performing safe substitutions
class SafeSub(dict):
    def __missing__(self, key):
        return "{%s}" % key


s = "{name} has {n} messages."

# (a) Simple substitution
name = "Guido"
n = 37
a = 99
print("a", a)
print(s.format_map(vars()))

"""
vars() 是一个内置函数，它返回当前作用域中的所有变量和它们的值的字典。在这个例子中，vars() 返回的字典包含了变量 name 和 n 的值。
"""
print("vars", vars())

# (b) Safe substitution with missing values
del n, a
"""
当 format_map 方法在 SafeSub 实例中找不到某个键时，__missing__ 方法会被调用。
在这个方法中，它返回一个包含占位符的字符串，而不是抛出 KeyError 异常。
这样就实现了安全的字符串格式化，即使某些占位符没有对应的变量，也不会导致程序崩溃。
"""

print(s.format_map(SafeSub(vars())))  # Guido has {n} messages.
# ! print("a", a) #  NameError: name 'a' is not defined

# (c) Safe substitution + frame hack
n = 37
import sys


def sub(text):
    """
    sys._getframe(1) 返回当前调用栈的上一层帧对象，f_locals 是这个帧对象的一个属性，它返回一个字典，包含了该帧的所有局部变量。
    """
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


print(sub("Hello {name}"))
print(sub("{name} has {n} messages"))
print(sub("Your favorite color is {color}"))
