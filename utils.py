from pymongo import MongoClient
def get_db_handle(db, host, port, username, password):

    client = MongoClient(host=host,
                        port=int(port),
                        username=username,
                        password=password
                        )
    db_handle = client['Books']
    return db_handle, client