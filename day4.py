# bmi caluculator(Underweight< 18.5, Normal 18.5 - 24.99,Overweight 25 - 29.99, Obese>30)
def bmi_caluculator(weight, height):
    h2 = height ** 2
    bmi_value = weight/h2
    if bmi_value < 18.5:
        return f"You'r Underweight as your bmi value is {bmi_value}."
    elif 18.5 <= bmi_value < 25:
        return f"You'r Normal as your bmi value is {bmi_value}."
    elif 25 <= bmi_value < 30:
        return f"You'r Overweight as your bmi value is {bmi_value}."
    else:
        return f"You'r Obese as your bmi value is {bmi_value}"


x = float(input("Enter weight in kilograms:"))
y = float(input("Enter height in meters:"))
print(bmi_caluculator(x, y))
