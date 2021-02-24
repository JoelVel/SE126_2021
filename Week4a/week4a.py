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
    print("First Name \t Lastname \t   age \tNickName \t\tHouse Alligence")

    for rec in file:

        records +=1
        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseally.append(rec[4])

        
       

        #print("{0:10} \t {1:12} \t {2:5} \t {3:5} \t\t {4:7}" .format(firstname[i], lastname[i], age[i], nickname[i], houseally[i]))

        if houseally == "House Stark":
            house1 += 1

        elif houseally == "House Tully":
            house2 += 1

        elif houseally == "House Lannister":
            house3 += 1

        elif houseally == "House Baratheon":
            house4 += 1

        elif houseally == "House Targaryen":
            house5 += 1
        
        elif houseally == "Night's Watch":
            house6 += 1

print("Total Amount of people: {}".format(records))

print("House stark: {}".format(house1))
print("House Tully: {}".format(house2))
print("House Lannister: {}".format(house3))
print("House Targaryen: {}".format(house4))
print("Night's Watch: {}".format(house6))
#print("average_age: {:.0f}".format(average_age))