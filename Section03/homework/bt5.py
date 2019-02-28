a = int(input("Plese enter your height(cm):"))
b = int(input("Plese enter your weight(kg):"))
a = a/100
BMI = b / (a*a)
if BMI < 16:
    print("Your BMI is Severely underweight")
if 16 < BMI < 18.5 :
    print("Your BMI is Underweight") 
if 18.5 < BMI < 25 :
    print("Your BMI is Normal")
if 25 < BMI < 30 :
    print("Your BMI is Overweight")
if BMI > 30 :
    print("Your BMI is Obese")




