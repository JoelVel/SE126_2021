import csv

desktops = 0
laptops = 0
old = 0
fairly_new = 0

with open("week3Laba/lab3a.csv") as csvLABa:
    
    file = csv.reader(csvLABa)
    
    for systems in file:
        
        computers = systems[0]
        years = systems[3]
    
        if computers == "D":
            
            computers = "Desktop"
            desktops += 1
            if years >= "16":
                years = "Old"
                old += 1
            
            elif years <= "16":
                years = "Fairly New"
                fairly_new += 1

        elif computers == "L":
            
            computers = "Laptop"         
            laptops += 1
            if years >= "16":
                years = "Old"
                old += 1
            
            elif years <= "16":
                years = "Fairly New"
                fairly_new += 1

            

    print("Desktops: {}, Laptops: {}".format(desktops, laptops))
    print("New Desktops and Laptops: {}, Fairly New Desktops and Laptops: {}".format(old, fairly_new))