rows = [
    {"address": "5412 N CLARK", "date": "07/01/2012"},
    {"address": "5148 N CLARK", "date": "07/04/2012"},
    {"address": "5800 E 58TH", "date": "07/02/2012"},
    {"address": "2122 N CLARK", "date": "07/03/2012"},
    {"address": "5645 N RAVENSWOOD", "date": "07/02/2012"},
    {"address": "1060 W ADDISON", "date": "07/02/2012"},
    {"address": "4801 N BROADWAY", "date": "07/01/2012"},
    {"address": "1039 W GRANVILLE", "date": "07/04/2012"},
]

from itertools import groupby
from pprint import pprint
from common.seperator import delimiter

# Sort by the desired field first
rows.sort(key=lambda r: r["date"])
# Iterate in groups
for date, items in groupby(rows, key=lambda r: r["date"]):
    print(date)
    for i in items:
        print("    ", i)

delimiter()
# Example of building a multidict
from collections import defaultdict

# A dictionary of lists
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row["date"]].append(row)
pprint(rows_by_date)

delimiter()
# Example of accessing specific values
date = "07/02/2012"
print("date", date)
for r in rows_by_date[date]:
    print(r)
