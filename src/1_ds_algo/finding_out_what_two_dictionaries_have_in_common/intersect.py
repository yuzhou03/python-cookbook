# example.py
#
# Find out what two dictionaries have in common
from common.text import print_pad

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}
print_pad("Find out what two dictionaries have in common")
print("a", a)
print("b", b)
print_pad("Result")
# Common keys: {'y', 'x'}
print("Common keys:", a.keys() & b.keys())
# Keys in a not in b: {'z'}
print("Keys in a not in b:", a.keys() - b.keys())
# (key,value) pairs in common: {('y', 2)}
print("(key,value) pairs in common:", a.items() & b.items())
