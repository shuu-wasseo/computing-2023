weight = float(input("weight in kg: "))
height = float(input("height in m : "))
bmi = weight/(height**2)
msg = (f"your bmi is {round(bmi, 2)}. ")
if bmi < 18.5:
    msg += "you are at risk of nutritional deficiency and osteoporosis."
elif bmi < 22.9:
    msg += "you are low-risk."
elif bmi < 27.4:
    msg += "you are moderate-risk."
else:
    msg += "you are high-risk."
print(msg)
