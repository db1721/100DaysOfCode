print("Welcome to the tip calculator")
bill = input("What is the total of the bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

total_per_person = ((float(tip_percentage) / 100 + 1) * float(bill) / int(people))

print(f"Each person should pay: ${round(total_per_person, 2)}")