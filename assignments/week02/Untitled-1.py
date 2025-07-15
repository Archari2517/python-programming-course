
weight = float(input("Enter your weight (meters) :"))
height = float(input("Enter your height (kilograms) :"))

BMI = weight / height ** 2

if BMI < 18.5 :
    print("Underweight")

if BMI >= 18.5 and BMI <= 24.9 :
    print("Underweight")

if BMI >= 25.0 and BMI <= 29.9 :
    print("Overweight")

if BMI >= 30.0 :
    print("Obese")