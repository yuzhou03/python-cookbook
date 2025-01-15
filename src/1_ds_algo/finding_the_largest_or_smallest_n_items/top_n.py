# example.py
#
# Example of using heapq to find the N smallest or largest items

import heapq

from common.seperator import delimiter

portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])

print("cheap", cheap)
print("expensive", expensive)

delimiter()
max_money = heapq.nlargest(1, portfolio, key=lambda s: s["price"] * s["shares"])
min_money = heapq.nsmallest(1, portfolio, key=lambda s: s["price"] * s["shares"])

print("max_money invested in ", max_money)
print("min_money invested in ", min_money)
delimiter()

max_share = heapq.nlargest(2, portfolio, key=lambda s: s["shares"])
min_share = heapq.nsmallest(2, portfolio, key=lambda s: s["shares"])
print("max_share", max_share)
print("min_share", min_share)
