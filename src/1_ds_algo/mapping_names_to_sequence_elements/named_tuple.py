# example.py
from collections import namedtuple

Stock = namedtuple("Stock", ["name", "shares", "price"])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        print(s)
        total += s.shares * s.price
    return total


# Some Data
records = [
    ("GOOG", 100, 490.1),
    ("ACME", 100, 123.45),
    ("IBM", 50, 91.15),
    ("FB", 80, 105.25),
    ("HPQ", 75, 33.25),
    ("YHOO", 25, 15.25),
]
print("total cost(sum of share * price):")
print(compute_cost(records))
