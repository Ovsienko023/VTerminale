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
        print(self.user_name, self.__password)
        find = self.coll_users.find_one({"user_name": self.user_name,
                                         "password": self.__password})
        print(find)
        if find:
            return True
        raise AuthenticationError("Method is_authentication in WrapperDB")

    def is_message(self):
        'Если БД скажет что: user_name == "Whom" and status == "not_view"'
        if self.user_name == "Whom" and status == "not_view":
            return True
        return False

    def seve_message(self):
        print('save_message')
        doc = dict()
        doc["user_name"] = self.user_name
        doc["whom"] = self.data["whom"]
        doc["data"] = self.data["data"]
        doc["message"] = self.data["message"]
        doc["status"] = "not_view"
        a = self.coll_message.save(doc)

    def check_message(self):
        print('check_message')
        data = self.coll_message.find({"whom": self.user_name,
                                       "status": "not_view"})
        pars_data = self.parsing(data)
        return pars_data

    def parsing(self, data):
        """ Parsing data in dict(dict()...) """
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

    def update_write_message(self, id):
        self.coll_message.update({'_id': ObjectId(id)},
                                 {'$set': {"status": "view"}})

    def save_user(self):
        """ Сохранение пользователя в БД(проверить что такого ещё нет) """

    def is_users(self):
        data = self.coll_users.find({"user_name": self.data['whom']})
        status = [user for user in data]
        if status:
            return True
        return False
    @classmethod
    def is_login(cls, user_name):
        db = ConnectDB().db
        coll_users = db.users
        data = coll_users.find({"user_name": user_name})
        status = [user for user in data]
        print(status)
        if status:
            return True
        return False
    
    @classmethod
    def save_reg_user(cls, user_name, data):
        db = ConnectDB().db
        coll_users = db.users
        password = data['password']

        doc = {"user_name": user_name, "password": password}
        if coll_users.save(doc):
            return True
        return False




# --- Использование
# db = ConnectDB().db
# coll = db.mycoll

# --- Найти по _id
# a = coll.find_one({"_id": ObjectId('5eaf9d2dd28025c76c4d896f')})
# print(a)

# --- Сохранение данных
# doc = {"name":"Иван", "surname":"Иванов"}
# coll.save(doc)


def creat_BD():
    db = ConnectDB().db
    # coll_message = db['message']
    coll_users = db.users
    # coll_message = db.message
    doc = {"user_name": "Marianne", "password": "jwebwei32r292294gIBI342G"}
    coll_users.save(doc)
    # data = coll_message.find({"whom":"kik", "status": "not_view"})
    # id = '5eb28c6e54f72ac038a814c7'
    # data = coll_message.find({"_id":ObjectId(id)})
    # coll_message.update({'_id': ObjectId(id)},
    #                     {'$set': {"status": "not_view"}})
    data = coll_users.find({})
    for i in data:
        print(i)
    # a = [r for r in data]
    # return data
    # for i in a:
    #     print(i)
# ObjectId('5eb28c6e54f72ac038a814c7')
# creat_BD()


def dell_users():
    db = ConnectDB().db
    coll_users = db.users
    coll_users.remove({'_id': ObjectId('5eb6fafbc5d51337a1cefa75')})
    data = coll_users.find({})
    for i in data:
        print(i)
# dell_users()

# {'password': '123', 'message': 'hi', 'whom': 'kik', 'data': 1588759662.14039}

# # --- Использование
# db = ConnectDB().db
# coll = db.message

# # --- Найти по _id
# a = coll.find_one({"_id": ObjectId('5eb28c6e54f72ac038a814c7')})
# print(a)
