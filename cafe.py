from flask import *
from bson.objectid import ObjectId
from cafedata import cafe_ndt


app = Flask(__name__)
app.config["SECRET_KEY"] ="searching cafe"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/listcafe')
def listcafe():
    all_cafes = cafe_ndt.find()
    return render_template('listcafe.html',all_cafes=all_cafes)


if __name__ == '__main__':
  app.run(debug=True)
 

