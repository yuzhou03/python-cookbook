from common.seperator import delimiter

"""
判断值相等
"""

# 数值比较
a = 10
b = 10
print("a == b", a == b)  # Output: True

# 列表比较
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2", list1 == list2)  # Output: True


"""
判断引用相等
is 用于比较两个对象是否是同一对象（即内存地址是否相同）。
如果两个变量指向的是同一个对象，则 is 返回 True。
"""
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b", a is b)  # Output: False (内容相等，但不是同一对象)
print("a is c", a is c)  # Output: True  (同一对象)
delimiter()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


# 创建对象
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person("Bob", 25)
print(person1, person2, person3)
# 比较
print("person1 == person2", person1 == person2)  # Output: True (内容相等)
print("person1 == person3", person1 == person3)  # Output: False (内容不同)
