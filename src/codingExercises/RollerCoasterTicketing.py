print("Welcome to the roller coaster!")
while True:
    ticket_price = 0
    height = int(input("What is you height in CM? "))

    if height >= 120:
        print('You can ride the roller coaster!')

        # Price for age
        age = int(input("What is your age? "))
        if age < 12:
            ticket_price += 5
        elif age <= 18:
            ticket_price += 7
        else:
            ticket_price += 12

        # Price for photo
        photo_check = True
        while photo_check:
            photo = input("Do you want a photo taken? Y or N: ")
            if photo.upper() in ['Y', 'YES']:
                ticket_price += 3
                photo_check = False
            elif photo.upper() in ['N', 'NO']:
                photo_check = False
            else:
                print("Please enter Y or N: ")

        print(f"Your total comes to ${ticket_price}")
    else:
        print("Sorry, you have to be taller to ride this roller coaster :(")