#Joel Velasquez, lab #1a
#room_size: room limit of people that can be in it
#people_amount: amount of people planning to attend the meeting
#people_out: people that can not attend due to spacing

answer = "y"

while answer == "y" or answer == "Y":

    room_size = int(input("\nPlease enter the legal limit of the room: "))

    people_amount = int(input("\nplease enter amount of people attending: "))

    if people_amount <= room_size:
        print("\nenough space for people")
    
    elif people_amount > room_size:
        print("\nroom too small")
        people_out = people_amount - room_size
        print("\n{} can not attend the meeting".format(people_out))
        print("\nonly {} can attend".format(room_size))

    answer = input("would you like to enter a new room's info? [y/n]")