import csv

id_ = []
name = []
age = []
color = []

records = 0

with open("demo6/binary.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:
        
        records += 1

        print(rec)

        id_.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])


print("Finished Processing file \n\n\n")

print("\n\n\n")

answer = "y"

while answer == "y":

    search = input("enter the NAME you are searching for: ")

    for i in range(0, records):

        if search == name[i]:
            print("we found them {0} at index: {1}".format(search, i))

    print("\nSearching finished")

    answer = input("search again? y for yes").lower()


#for i in range(0, records):
    #print("{0}\t{1}\t{2}\t{3}".format(id_[i], name[i], age[i], color[i]))