import csv

records = 0
house1 = 0
house2 = 0
house3 = 0
house4 = 0
house5 = 0
house6 = 0

firstname = []
lastname = []
age = []
nickname = []
houseally = []

with open("Week4a/lab4A_GOT_NEW.txt") as csvfile:
    
    file = csv.reader(csvfile)
    print("First Name \t Lastname \t\t\tage \tNickName \t\tHouse Alligence")

    for rec in file:

        records +=1
        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseally.append(rec[4])

    for i in range(0, records):   
       

        print("{0:15} \t{1:15} \t{2:1} \t{3:1} \t\t{4:15}".format(firstname[i], lastname[i], age[i], nickname[i], houseally[i]))

    for i in range(records):

        if houseally[i] == "House Stark":
            house1 += 1

        elif houseally[i] == "House Tully":
            house2 += 1

        elif houseally[i] == "House Lannister":
            house3 += 1

        elif houseally[i] == "House Baratheon":
            house4 += 1

        elif houseally[i] == "House Targaryen":
            house5 += 1
        
        elif houseally[i] == "Night's Watch":
            house6 += 1
    
    for i in range(records):
        average_age = age[i] + age[i] / records

print("Total Amount of people: {}".format(records))

print("House stark: {}".format(house1))
print("House Tully: {}".format(house2))
print("House Lannister: {}".format(house3))
print("House Baratheon: {}".format(house4))
print("House Targaryen: {}".format(house5))
print("Night's Watch: {}".format(house6))
print("average age: {:.0f}".format(average_age))