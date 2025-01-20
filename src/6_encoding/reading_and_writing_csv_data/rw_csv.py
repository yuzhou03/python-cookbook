# example.py
#
# Various samples of reading CSV files

import csv
from common.text import print_pad

# (a) Reading as tuples

print_pad("Reading as tuples:")
with open("stocks.csv") as f:
    # f_csv 是一个 CSV 读取器对象，通常是通过 csv.reader() 函数创建的。
    f_csv = csv.reader(f)
    # next(f_csv) 会读取 CSV 文件的第一行数据
    headers = next(f_csv)
    for row in f_csv:
        # process row
        print("    ", row)

# (b) Reading as namedtuples

print_pad("Reading as namedtuples")
from collections import namedtuple

with open("stocks.csv") as f:
    f_csv = csv.reader(f)
    Row = namedtuple("Row", next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Process row
        print("    ", row)


# (c) Reading as dictionaries

print_pad("Reading as dicts")
with open("stocks.csv") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print("    ", row)

# (d) Reading into tuples with type conversion

print_pad("Reading into named tuples with type conversion")

col_types = [str, float, str, str, float, int]
with open("stocks.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

# (e) Converting selected dict fields

print_pad("Reading as dicts with type conversion")

field_types = [("Price", float), ("Change", float), ("Volume", int)]

with open("stocks.csv") as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)
