# calculate bmi
weight = float(input("輸入體重:"))
height = float(input("輸入身高:"))
bmi = weight / (height / 100) ** 2
print("體重是:" + str(weight))
print("身高是:", height)
print("BMI:", bmi)

if bmi >= 25:
    print("過重")
    print("多運動")
elif bmi >= 18:
    print("正常")
else:
    print("過輕")
print("!!!!")