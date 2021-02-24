#def divi_ave():
    

import csv

with open("Midterm project/Games.csv") as games_sold:

    file = csv.reader(games_sold)

    for games in file: 
        