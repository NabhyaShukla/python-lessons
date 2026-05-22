# Write a program which takes height and weight as input from the user
# calculates BMI = weight/ (height/100)**2 , displays different categories

height = float(input("Enter Your height in cm : "))
weight = float(input("Enter Your weight in kg : "))

BMI = weight / (height / 100) ** 2

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are obese")
elif BMI <= 39.9:
    print("You are severely obese")
else:
    print("You are severely obese")

if height == 0:
    print("Height cannot be zero")
if weight == 0:
    print("Weight cannot be zero")