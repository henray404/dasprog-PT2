weight = float(input("input your weight: "))
height = float(input("input your height: "))

weight = weight * 2.2046
height = height * 0.3937

bmi = (703 * weight) / (height ** 2)

if bmi < 18.5:
    print("you are underweight")
    status = "underweight"
elif bmi < 25:
    print("you are normal weight")
    status = "normal weight"
elif bmi < 30:
    print("you are overweight")
    status = "overweight"
else:
    print("you are obese")
    status = "obese"

print(f"Your BMI is {bmi:.2f}, which is considered {status}.")
