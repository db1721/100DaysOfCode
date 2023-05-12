while True:
    num = input("Enter a number to see if it is odd or even: ")

    if int(num) % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")