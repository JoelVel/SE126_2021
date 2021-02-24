import csv

records = 0

name = []
age = []
animal = []
color = []
number = []

with open("week2_finished/classList.text") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        record+=1
