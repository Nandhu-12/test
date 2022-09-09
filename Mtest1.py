import pymongo
client = pymongo.MongoClient("mongodb+srv://Nandhini:MONGO2412!@mongo-cluster.p7389rv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Nandhu",
    "email" : "aabbcc@gmail.com",
    "surname" : "saro"
}

d = {
    "name" : "Nandhu1",
    "email" : "aabbcc@gmail.com",
    "surname" : "saro"
}
d = {
    "name" : "Nandhu2",
    "email" : "aabbcc@gmail.com",
    "surname" : "saro"
}
db1 = client['Mtest1']
coll = db1['test']
coll.insert_one(d)