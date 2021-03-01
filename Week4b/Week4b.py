import csv

firstname = []
lastname = []
age = []
nickname = []
houseally = []

records = 0

with open("Week4b/lab4A_GOT_NEW.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseally.append(rec[4])


    print("\n1.Print all First, Last, and nicknames \n2.Print Last names with House Allegiance and Motto \n3.Print full records \n4.EXIT")

    choices = input("What action would you like to do?: ")

            
   
    if choices == "1":
        print("first name \t\tlast name \t\tnickname\n")
        for i in range(0, records):
            print("{0:15} \t{1:15} \t{2:1}".format(firstname[i], lastname[i], nickname[i]))

    if choices == "2":
        print("last name \tHouse Allegiance\n")
        for i in range(records):
            print("{0:15} \t{1:15}".format(lastname[i], houseally[i]))

    if choices == "3":
        print("First Name \t Lastname \t\t\tage \tNickName \t\tHouse Alligence\n")
        for i in range(0, records):   
                print("{0:15} \t{1:15} \t{2:1} \t{3:1} \t\t{4:15}".format(firstname[i], lastname[i], age[i], nickname[i], houseally[i]))

    elif choices == "4":
        print("thank you for using the program. goodbye")
            