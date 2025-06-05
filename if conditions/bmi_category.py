import math

height=float(input("Enter your height in metre"))
weight=float(input("Enter your weight in KG"))
BMI=weight/(height*height)
print(BMI)

if BMI >= 30:
    print("Obesity")
elif BMI >25 and BMI<=29:
    print("Overweight")
elif BMI >=18.5 and BMI<=25:
    print("Normal")
elif BMI <18.5:
    print("Underweight")

