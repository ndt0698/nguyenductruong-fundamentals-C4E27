from pymongo import MongoClient

mongo_uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

rv = client.c4e

rivers_colection = rv["river"]