from pymongo import MongoClient
from bson.objectid import ObjectId
mongo_uri = "mongodb+srv://admin:admin@cluster0-kb7pi.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)
cafe_app = client.Cafeshop
cafe_ndt = cafe_app["cafes"]

# print(cafe_ndt)

# Highlands_Coffee_TheManor = {
    
#     "Name":" Highlands Coffee The Manor",
#     "Address":"1A, TheManor, Mễ Trì, Nam Từ Liêm, Hà Nội",
#     "Menu":"Cafe phin, Cafe Espresso, Freezes, Cakes",
#     "Contacts": "(04) 3794.0441"
# }
# Highlands_Coffee_Chelsea = {
    
#     "Name":"Highlands Coffee Chelsea",
#     "Address":"Tòa nhà Chelsea Park, Trung Kính, Phường Trung Hòa, Quận Cầu Giấy, Hà Nội",
#     "Menu":"Cafe phin, Cafe Espresso, Freezes, Cakes",
#     "Contacts": "(04) 3782.4960"
# }
# Highlands_Coffee_Indochina = {
    
#     "Name":"Highlands Coffee Indochina",
#     "Address":"241 Xuân Thủy, Quận Cầu Giấy, Hà Nội",
#     "Menu":"Cafe phin, Cafe Espresso, Freezes, Cakes",
#     "Contacts":"(04) 3795.4029"
# }
# Highlands_Coffee_TimesCity = {
    
#     "Name":"Highlands_Coffee_TimesCity",
#     "Address":"458 Minh Khai, Quận Hai Bà Trưng, Hà Nội",
#     "Menu":"Cafe phin, Cafe Espresso, Freezes, Cakes",
#     "Contacts":"(04) 3200.9069"
# }
# Highlands_Coffee_Opera = {
    
#     "Name":"Highlands_Coffee_Opera",
#     "Address":"	1A Tràng Tiền,Phường Tràng Tiền, Quận Hoàn Kiếm, Hà Nội",
#     "Menu":"Cafe phin, Cafe Espresso, Freezes, Cakes",
#     "Contacts":"(04) 3933.4947"
# }

# AHA_Coffee_ToHieu = {
#     "Name":"AHA Coffee Tô Hiệu",
#     "Address":"233 Tô Hiệu, Cầu Giấy, Hà Nội",
#     "Menu":"Cafe, Ice cream, Teas, Juices",
#     "Contacts":"096.556.1717"
# }

# cafe_ndt.insert_one(Highlands_Coffee_TheManor)
# cafe_ndt.insert_one(Highlands_Coffee_Chelsea)
# cafe_ndt.insert_one(Highlands_Coffee_Indochina)
# cafe_ndt.insert_one(Highlands_Coffee_TimesCity)
# cafe_ndt.insert_one(Highlands_Coffee_Opera)
# cafe_ndt.insert_one(AHA_Coffee_ToHieu)


