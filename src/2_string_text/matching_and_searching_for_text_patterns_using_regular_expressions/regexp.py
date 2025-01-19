# example.py
#
# Examples of simple regular expression matching

import re
from common.text import print_pad

# Some sample text
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
print_pad("Some sample text")
print(text)

# (a) Find all matching dates
print_pad("Find all matching dates")
datepat = re.compile(r"\d+/\d+/\d+")
print(datepat.findall(text))

# (b) Find all matching dates with capture groups
print_pad("Find all matching dates with capture groups")
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
for month, day, year in datepat.findall(text):
    print("{}-{}-{}".format(year, month, day))

# (c) Iterative search
print_pad("Iterative search")
for i, m in enumerate(datepat.finditer(text), start=1):
    month, day, year = m.groups()
    print(i, m.groups(), "{}-{}-{}".format(year, month, day))
