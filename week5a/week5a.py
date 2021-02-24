import csv

records = 0

firstname = []
lastname = []
dob = []

with open("week5a/lab5_updated.txt") as csvfile:
    
    file = csv.reader(csvfile)

        for rec in file:

            records +=1

