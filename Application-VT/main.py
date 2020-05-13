import json
from scripts.server.server import app
import sys


def main():
    app.run(*conf_server())

OS = sys.platform

def conf_server():
    """ returns tuple(host, server) from the file: config.txt """
    if OS == 'win32':
        with open('Application-VT\config.txt') as config:
            json_str = config.read()
            json_str = json.loads(json_str)
        host = json_str['server']['host']
        port = json_str['server']['port']
        return host, port
    else:
        print('!!')
        with open('Application-VT/config.txt') as config:
            json_str = config.read()
            json_str = json.loads(json_str)
        host = json_str['server']['host']
        port = json_str['server']['port']
        return host, port


if __name__ == "__main__":
    main()
# import sys

# print(sys.platform)
# import pymongo


# # info_db = {"host": "mongodb://127.0.0.1", "port": 27017}
# conn = pymongo.MongoClient(host="mongodb://127.0.0.1", port=27017)
# # conn = pymongo.MongoClient(*info_db)
# # print(*info_db)
# db = conn.mydb
# coll_users = db.users

# # doc = {"user_name": "bob", "password": "123"}
# # coll_users.save(doc)


# data = coll_users.find({})
# for i in data:
#     print(i)