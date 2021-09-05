name = "Avaneesh"
height_m = 1778
weight_kg = 70
bmi = weight_kg / (height_m * height_m)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
