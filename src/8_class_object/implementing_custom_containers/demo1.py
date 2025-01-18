# Example of a custom container

"""
在 Python 3.9 及以后版本中，Sequence 类已经从 collections 模块移到了 collections.abc 模块。
collections.abc 模块提供了一些抽象基类（ABC），这些 ABC 可以用来定义自定义容器的行为。
"""
from collections.abc import Sequence
import bisect


class SortedItems(Sequence):
    def __init__(self, initial=None):
        if initial is None:
            self._items = []
        else:
            self._items = sorted(initial)

    # Required sequence methods
    def __getitem__(self, index):
        if not self._items:
            raise IndexError("Index out of range")
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


if __name__ == "__main__":
    items = SortedItems([5, 1, 3])
    print("list(items)", list(items))
    print("items[0]", items[0])

    print("items[-1]", items[-1])
    items.add(2)
    print(list(items))
    items.add(-10)
    print(list(items))
    print("items[1:4]", items[1:4])
    print("3 in items", 3 in items)
    print("len(items)", len(items))
    for n in items:
        print(n)
