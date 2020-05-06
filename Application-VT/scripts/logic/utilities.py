import pymongo
import os
import json
from bson.objectid import ObjectId

class AuthenticationError(Exception):
    pass


class ConnectDB():
    def __init__(self):
        self.info_db = self.get_info_db()
        self.conn = pymongo.MongoClient(*self.info_db)
        self.db = self.conn.mydb

    def config_app(self):
        path = os.getcwd() + "/Application-VT/config.txt"
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def get_info_db(self):
        info_db = self.config_app()['Data_Base']
        host, port = info_db['host'], info_db['port']
        return host, int(port)




class WrapperDB:
    def __init__(self, user_name, data):
        self.db = ConnectDB().db
        self.coll_users = self.db.users
        self.coll_message = self.db.message
        self.user_name = user_name 
        self.__password = data["password"]
        self.authentication = self.is_authentication()
        self.data = data
       
    def is_authentication(self):
        find = self.coll_users.find_one({"user_name": self.user_name,
                                            "password": self.__password})
        # print(find)
        if find:
            return True
        raise AuthenticationError("Method is_authentication in WrapperDB")

    def is_user(self):
        if self.user_name in list_users:
            return True
        return False
    
    def is_message(self):
        'Если БД скажет что: user_name == "Whom" and status == "not_view"'
        if self.user_name == "Whom" and status == "not_view":
            return True
        return False
# doc = {"name":"Иван", "surname":"Иванов"}
# coll.save(doc)
    def seve_message(self):
        print('save_message')
        doc = dict()
        doc["user_name"] = self.user_name
        doc["whom"] = self.data["whom"]
        doc["data"] = self.data["data"]
        doc["message"] = self.data["message"]
        doc["status"] = "not_view"
        a = self.coll_message.save(doc)
        print(a)
        
        
    
    def save_user(self):
        """ Сохранение пользователя в БД(проверить что такого ещё нет) """
    
    def get_message(self):
        """ Даёт все сообщения где: (user_name == "Whom" and status == "not_view") """








# # --- Использование
# db = ConnectDB().db
# coll = db.mycoll

# # --- Найти по _id
# a = coll.find_one({"_id": ObjectId('5eaf9d2dd28025c76c4d896f')})
# print(a)

#--- Сохранение данных
# doc = {"name":"Иван", "surname":"Иванов"}
# coll.save(doc)



# def creat_BD():
#     db = ConnectDB().db
#     # coll_message = db['message']
#     coll_users = db['users']
#     # doc = {"user_name":"bob", "password":"123"}
#     # coll_users.save(doc)
#     a = coll_users.find_one({"user_name": "bob", "password":"123"})
#     print(a)
# creat_BD()

# {'password': '123', 'message': 'hi', 'whom': 'kik', 'data': 1588759662.14039}

# --- Использование
db = ConnectDB().db
coll = db.message

# --- Найти по _id
a = coll.find_one({"_id": ObjectId('5eb28c6e54f72ac038a814c7')})
print(a)