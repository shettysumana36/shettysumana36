import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())
mydb=myclient["cmrec"]
'''mydblist=myclient.list_database_names()
if "cmrec1" in mydblist:
    print("database is exists")
else:
    print("database does not exists")
'''
mycol=mydb["csea"]
'''
mylist=mydb.list_collection_names()
if "csea1" in mylist:
    print("is exists")
else:
    print("does not exists")
'''
mydict={"name":"trisha reddy","Rollno":"228r1a0550"}
x=mycol.insert_one(mydict)
x=mycol.insert_many