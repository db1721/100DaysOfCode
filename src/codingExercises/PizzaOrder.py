def pepperoni(size):
    """
    Calculate Pepperoni cost
    :param size: Size of pizza
    :return: Cost to add
    """
    if size.upper() in ('S', 'SMALL'):
        return 2
    else:
        return 3

while True:
    print("Welcome to Python Pizza Deliveries")

    # Variables
    total_bill = 0
    size = ''
    size_check = True
    topping_list = ['pepperoni', 'extra cheese']

    # Check what pizza size user wants
    while size_check:
        size = input("What size pizza do you want? S, M, L: ")
        if size.upper() in ('S', 'SMALL'):
            total_bill += 15
            size_check = False
        elif size.upper() in ('M', 'MEDIUM'):
            total_bill += 20
            size_check = False
        elif size.upper() in ('L', 'LARGE'):
            total_bill += 25
            size_check = False
        else:
            print("Please enter S, M, or L: ")

    # Check what topping user wants
    for topping in topping_list:
        topping_check = True
        while topping_check:
            topping_prompt = input(f"Would you like to add {topping}: ")
            if topping_prompt.upper() in ('Y', 'YES'):
                if topping == "extra cheese":
                    total_bill += 1
                elif topping == 'pepperoni':
                    total_bill += pepperoni(size)
                topping_check = False
            elif topping_prompt.upper() in ('N', 'NO'):
                topping_check = False
            else:
                print("Please enter Y or N: ")

    print(f"Your final bill is: ${total_bill}")

