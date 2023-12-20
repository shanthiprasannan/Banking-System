weight=float(input("Enter your weight in (kg)"))
height=float(input("Enter your height in metres"))
bmi=weight/height
if bmi<18.5:
    print("Your BMI is:", bmi,"\nYou are in the “Underweight” range.")
elif bmi>=18.5 and bmi<=24.:
    print("Your BMI is:", bmi,"\nYou are in the “Normal” range.")
elif bmi>=25 and bmi<=29.9:
    print("Your BMI is:", bmi,"\nYou are in the “Overweight” range.")
elif bmi>=30:
    print("Your BMI is:", bmi,"\nYou are in the “Obese” range.")



