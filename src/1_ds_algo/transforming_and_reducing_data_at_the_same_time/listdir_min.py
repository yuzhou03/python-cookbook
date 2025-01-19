# example.py
#
# Some examples of using generators in arguments

import os
from common.text import print_pad, delimiter


def check_python_files(directory):
    files = os.listdir(os.path.expanduser(directory))
    print("Python files:", files)

    if any(name.endswith(".py") for name in files):
        print("There be python files!")
    else:
        print("Sorry, no python files.")


paths = ["~/Documents", "."]

for p in paths:
    delimiter()
    print_pad(f"checking path: {os.path.abspath(p)}")
    check_python_files(p)


# Output a tuple as CSV
delimiter()
s = ("ACME", 50, 123.45)
print("join of iterables", ",".join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {"name": "GOOG", "shares": 50},
    {"name": "YHOO", "shares": 75},
    {"name": "AOL", "shares": 20},
    {"name": "SCOX", "shares": 65},
]
min_shares = min(s["shares"] for s in portfolio)
print_pad("min_shares")
print("portfolio", portfolio)
print("min_shares", min_shares)
