"""
一、高阶函数的定义
1. 什么是高阶函数？
接受函数作为参数：函数可以作为参数传递给另一个函数。
返回函数作为结果：函数可以作为另一个函数的返回值。
操作函数：高阶函数可以对函数进行组合、转换等操作。

2. 为什么使用高阶函数？
代码复用：通过将通用逻辑抽象为高阶函数，减少重复代码。
灵活性：允许动态传递行为（函数）给其他函数。
函数式编程风格：支持声明式编程，代码更简洁易读。

六、高阶函数的应用场景
数据处理：
使用map和filter对列表进行转换和过滤。
使用reduce对数据进行聚合。

回调机制：
在事件驱动编程中，将函数作为回调传递给事件处理器。

动态行为：
通过高阶函数实现策略模式或插件机制。

函数组合：
将多个简单函数组合成复杂逻辑。


七、注意事项

性能问题：
高阶函数可能引入额外的函数调用开销，需注意性能影响。
在性能敏感场景中，优先使用列表推导式或生成器表达式替代map和filter。

可读性：
过度使用高阶函数可能导致代码难以理解，需权衡简洁性与可读性。

调试难度：
高阶函数的调试可能比普通函数更复杂，建议使用清晰的命名和注释。
"""

from common.text import print_pad


def sort_by_length(fruits):
    # Sorting a list of words by length
    print_pad("Sorting a list of words by length")
    sorted_fruits = sorted(fruits, key=len)
    # 输出: ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
    print(sorted_fruits)


def sorted_by_reverse(fruits):
    # Sorting a list of words by their reversed spelling
    print_pad("Sorting a list of words by their reversed spelling")
    fruits = sorted(fruits, key=lambda word: word[::-1])
    print(fruits)


def main():
    fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
    sort_by_length(fruits)
    sorted_by_reverse(fruits)


if __name__ == "__main__":
    main()
