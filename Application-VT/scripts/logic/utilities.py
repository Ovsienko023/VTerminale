import pymongo
import os
import json
import sys
from bson.objectid import ObjectId


OS = sys.platform


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


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class WrapperDB:
    def __init__(self):
        self.db = ConnectDB().db
        self.coll_users = self.db.users
        self.coll_message = self.db.message

    #!Норм
    def is_authentication(self, login, password):
        print(login, password)
        find = self.coll_users.find_one({"user_name": login,
                                         "password": password})
        print(find)
        if find:
            return True
        return False
    #!Норм    
    def registration(self, login, password):
        doc = {"user_name": login, "password": password}
        if self.coll_users.save(doc):
            return True
        return False
    #!Норм
    def is_user(self, login):
        data = self.coll_users.find({"user_name": login})
        status = [user for user in data]
        if status:
            return True
        return False
    #!Норм
    def seve_message(self, doc):
        status = self.coll_message.save(doc)
        if status:
            return True
        return False

    def check_message(self, login):
        print('check_message')
        data = self.coll_message.find({"whom": login,
                                       "status": "not_view"})
        return data

    def update_write_message(self, id):
        self.coll_message.update({'_id': ObjectId(id)},
                                 {'$set': {"status": "view"}})
    

class Destributor:
    def __init__(self, login, password, data=None):
        self.user = User(login, password)
        self.authentication = WrapperDB().is_authentication(login, password)
        self.data = data

    def registration(self):
        login = self.user.login
        password = self.user.password
        if not WrapperDB().is_user(login):
            status = WrapperDB().registration(login, password)
            return status
        return 'Login already in uselogin'

    def seve_message(self, data):
        print('save_message')
        doc = dict()
        doc["user_name"] = self.user.login
        doc["whom"] = self.data["whom"]
        doc["data"] = self.data["data"]
        doc["message"] = self.data["message"]
        doc["status"] = "not_view"
        status = WrapperDB().seve_message(doc)
        return status

    def is_whom_user(self, data):
        whom = data['whom']
        status = WrapperDB().is_user(whom)
        return status

    def check_message(self):
        message = WrapperDB().check_message(self.user.login)
        pars_data = self.parsing(message)
        return pars_data

    def parsing(self, data):
        """ Parsing data in dict(dict()...) """
        for i in data:
            print(i)
        try:
            new_data = dict()
            new_data['messages'] = []
            for mess in data:
                id = mess['_id']
                self.update_write_message(id)
                del mess['_id']
                new_data['messages'].append(mess)
            return new_data
        except TypeError:
            return None














#     @classmethod
#     def is_login(cls, user_name):
#         db = ConnectDB().db
#         coll_users = db.users
#         data = coll_users.find({"user_name": user_name})
#         status = [user for user in data]
#         print(status)
#         if status:
#             return True
#         return False
    
#     
# # --- Использование
# # db = ConnectDB().db
# # coll = db.mycoll

# # --- Найти по _id
# # a = coll.find_one({"_id": ObjectId('5eaf9d2dd28025c76c4d896f')})
# # print(a)

# # --- Сохранение данных
# # doc = {"name":"Иван", "surname":"Иванов"}
# # coll.save(doc)


def creat_BD():
    db = ConnectDB().db
    # coll_message = db['message']
    coll_users = db.users
    coll_message = db.message
    # doc = {"user_name": "Marianne", "password": "jwebwei32r292294gIBI342G"}
    # coll_users.save(doc)
    # data = coll_message.find({"whom":"kik", "status": "not_view"})
    # id = '5eb28c6e54f72ac038a814c7'
    # data = coll_message.find({"_id":ObjectId(id)})
    # coll_message.update({'_id': ObjectId(id)},
    #                     {'$set': {"status": "not_view"}})
    data = coll_message.find({})
    for i in data:
        print(i)
    # a = [r for r in data]
    # return data
    # for i in a:
    #     print(i)
# # ObjectId('5eb28c6e54f72ac038a814c7')
# creat_BD()


def dell_users():
    db = ConnectDB().db
    coll_users = db.users
    coll_users.remove({'_id': ObjectId('5ebbb0594ae3353b058914c2')})
    data = coll_users.find({})
    for i in data:
        print(i)
# dell_users()

# # {'password': '123', 'message': 'hi', 'whom': 'kik', 'data': 1588759662.14039}

# # # --- Использование
# # db = ConnectDB().db
# # coll = db.message

# # # --- Найти по _id
# # a = coll.find_one({"_id": ObjectId('5eb28c6e54f72ac038a814c7')})
# # print(a)
