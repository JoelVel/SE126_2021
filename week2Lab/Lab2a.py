import csv

room_records = 0

with open("week2\Lab2a.py") as csvLABa:
    file = csv.reader(csvLABa)
    for name in file