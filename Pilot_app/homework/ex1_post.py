from pymongo import MongoClient

mongo_uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

Exercise_1 = client.c4e
my_opinion = Exercise_1["posts"]

opinion = {
    "title":"Bốc bát họ đeeeee",
    "author":"Nguyễn Đức Trường",
    "content":"Bốc bát 20 đảm bảo cầm về 16 "
}

my_opinion.insert_one(opinion)

