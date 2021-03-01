import csv

id = []
name = []
age = []
color = []

records = 0

with open("week6/binary-1.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:
        records += 1

