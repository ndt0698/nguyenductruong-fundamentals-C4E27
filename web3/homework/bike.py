from flask import *
from bson.objectid import ObjectId
from bike_db import bikes

app = Flask(__name__)


@app.route('/')
def homebike():
    return render_template('home-bike.html')
@app.route('/new_bike', methods=["GET","POST"])
def new_bike():
    if  request.method == "GET":
        return render_template('new_bike.html')
    elif request.method == "POST":
        form = request.form 
        bike_model = form["model"]
        bike_dailyfree = form["dailyfee"]
        bike_image = form["image"]
        bike_year = form["year"]


        new_bikes_value = {  
                "model": bike_model,
                "dailyfee": bike_dailyfree,
                "image": bike_image,
                "year": bike_year,
            }
    
    bikes.insert_one(new_bikes_value)
    return render_template('new_bike.html')










if __name__ == '__main__':
    app.run(debug=True)
