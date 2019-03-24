from flask import Flask, render_template, redirect
about = Flask(__name__)

@about.route('/')
def home():
   return "From NĐT with love"


@about.route('/about-me')
def profile():
   return render_template("profile.html")


@about.route('/school')
def techkid():
   return redirect("http://techkids.vn")


if __name__ == '__main__':
   about.run(debug=True)

