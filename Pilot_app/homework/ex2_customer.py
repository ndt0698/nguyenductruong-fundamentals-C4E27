from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
cus = client.get_database()

customers = cus['customers']

events = 0
wom = 0 
ads = 0 

all_customers = list(customers.find())
for customers in all_customers:
    if customers["ref"] == "events":
        events = events + 1
    elif customers["ref"] == "wom":
        wom = wom + 1
    elif customers["ref"] == "ads":
        ads = ads + 1

print("events:",events)
print("wom:",wom)
print("ads:",ads)


name_ref = "events", "wom", "ads"
count_ref = [3902,1134,1939]

pyplot.pie(count_ref, labels=name_ref,autopct="%.1f%%",shadow=True, explode=[0,0,0.1])
pyplot.title("Đồ thị của em đã ổn áp chưa anh Đạt  :)) ")
pyplot.axis("equal")
pyplot.show()