
from datetime import date

first_date = date(int(input("Year 1: ")), int(input("Mon 1: ")), int(input("Day 1: ")))
second_date = date(int(input("Year 2: ")), int(input("Mon 2: ")), int(input("Day 2: ")))
delta = abs(second_date - first_date)
print(delta.total_seconds())