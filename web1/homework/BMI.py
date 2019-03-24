from flask import Flask, render_template
bmi = Flask(__name__)


@bmi.route('/')
def ndt():
    return "From NĐT with love"



#Sử dụng template
# @bmi.route('/bmi/<int:weight>/<int:height>')
# def calculate(weight,height):
#     height = height / 100
#     BMI = (weight/(height*height))
#     return render_template('BMI.html',BMI = BMI)

#Không sử dụng template

@bmi.route('/bmi/<int:weight>/<int:height>')
def calculate(weight,height):
    height = height / 100
    BMI = (weight/(height*height))
    print("Your BMI is :", BMI)
    if BMI < 16:
        said = "You are Severely underweight !"
    elif 16 <= BMI < 18.5:
        said ="You are Underweight !"
    elif 18.5 <= BMI < 25:
        said = "You are Normal !"
    elif 25 <= BMI < 30:
        said = "You are Overweight !"
    elif BMI > 30:
        said = "You are Obese !"
    return "Your BMI is:" + str(BMI) +  said


if __name__ == '__main__': 
  bmi.run(debug=True)   