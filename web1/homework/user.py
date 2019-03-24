from flask import Flask, render_template
user = Flask(__name__)

@user.route('/')
def ndt():
    return "From NĐT with love"

@user.route('/user/<username>')
def facebook():
    users = {
        {"Truong": {
        "name" : "Nguyễn Đức Trường",
        "age": "21",
        "gender": "Male"
        },
        "Quan" : {
        "name" : " Nguyễn Anh Quân",
        "age": "23",
        "gender":"Female =))"
        }
        }
    }

    return render_template("users.html",
                            facebook=users)

if __name__ == '__main__': 
  user.run(debug=True)