name = input("Enter your name: ")
height = float(input("Enter your height in centimeteres: "))
weight = float(input("Enter your weight in Kg: "))
height = height / 100
BMI = weight / (height * height)
print("Your BMI is: ", BMI)
if BMI > 0:
    if BMI <= 16:
        print("You are severely underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("You are healthy")
    elif BMI <= 30:
        print("You are severly overweight")
    else:
        ("I am too smart for you so enter the correct values")
