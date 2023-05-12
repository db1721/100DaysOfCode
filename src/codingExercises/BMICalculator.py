height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight/(height**2))

final_print_out = f"Your BMI is {bmi}, you are "
if bmi < 18.5:
    final_print_out += "underweight"
elif 18.5 < bmi < 25:
    final_print_out += "normal weight"
elif 25 < bmi < 30:
    final_print_out += "overweight"
elif 30 < bmi < 35:
    final_print_out += "obese"
else:
    final_print_out += "clinically obese"

print(final_print_out)