from pymongo import MongoClient
import pymongo

# def get_db_handle(db, host, port, username, password):

#     client = MongoClient(host=host,
#                         port=int(port),
#                         username=username,
#                         password=password
#                         )
#     db_handle = client['Books']
#     return db_handle, client    

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Cars"]
mycol = mydb["cardb2"]