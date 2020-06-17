import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import chat_v1

import requests
import json
import time
import sys
import os

HOST = "http://192.168.16.70:5555/"

def get_config():
    
    path = os.getcwd() + "\config.json"
    print(path)
    with open(path)as r:
        data = r.read()
        conf_dict = json.loads(data)
    return conf_dict


class User:
    def __init__(self):
        self.login = self.get_login()
        self.password = self.get_password()

    def get_login(self):
        name = get_config()['login']
        return name

    def get_password(self):
        password = get_config()['password']
        return password

    def chenge_user(self, login, password):
        conf = get_config()
        conf['login'] = login
        conf['password'] = password
        with open('config.conf', 'w')as w:
            json_dict = json.dumps(conf)
            w.write(json_dict)


class Message:
    def __init__(self, message):
        self.message = message


class RequestServ:
    def __init__(self):
        self.login = User().login
        self.password = User().password
        self.host = get_config()['host']
        self.url_registration = self.host + r'api/v2/registration/'
        self.url_is_login = self.host + r'api/v2/is_login/'
        self.url_authentication = self.host + f'api/v2/{self.login}/authentication/'
        self.url_is_whom_login = self.host + f'api/v2/{self.login}/is_whom_login/'
        self.url_write_message = self.host + f'api/v2/{self.login}/write_message/'
        self.url_read_message = self.host + f'api/v2/{self.login}/read_message/'
        self.url_check_message = self.host + f'api/v2/{self.login}/check_message/'

    def registration(self, login, password) -> dict:
        data = {"login": login,
                "password": password}
        status = requests.post(self.url_registration, json=data)
        return status.json()

    def authentication(self):
        data = {"password": self.password}
        status = requests.post(self.url_authentication, json=data)
        return status.json()

    def is_whom_login(self, whom):
        data = {"password": self.password,
                "whom": whom}
        status = requests.post(self.url_is_whom_login, json=data)
        return status.json()

    def write_message(self, whom, message):
        data = {"password": self.password,
                "message": message,
                "whom": whom,
                "data": time.time()}
        status = requests.post(self.url_write_message, json=data)
        return status.json()

    def read_message(self):
        data = {"password": self.password}
        status = requests.post(self.url_read_message, json=data)
        return status.json()

    def check_message(self):
        data = {"password": self.password}
        status = requests.post(self.url_check_message, json=data)
        return status.json()

    def is_login(self, login):
        data = {"login": login}
        status = requests.post(self.url_is_login, json=data)
        return status.json()





class Chat(QtWidgets.QMainWindow, chat_v1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_message)
        self.pushButton_2.clicked.connect(self.read_message)
        
    def send_message(self):
        print('Нажатие на кнопку Send')
        text_message = self.writeMessage.toPlainText()
        whom = self.writeMessage_2.toPlainText()
        status = RequestServ().write_message(whom, text_message)
        print(status)
        # self.viewMessage.append(status.content.decode())
    
    def read_message(self):
        print('Чтение сообщения')

        data = RequestServ().read_message()
        print(type(data), data)
        if data['status']:   
            for mes in data['messages']:
                print(f"{mes['user_name']}: {mes['message']}\ntime: {self.pars_time(mes['data'])}\n")
                mess = f"{mes['user_name']}: {mes['message']}\ntime: {self.pars_time(mes['data'])}\n"
                self.viewMessage.append(mess)

# def pars_message(data):
#     for mes in data['messages']:
#         print(f"{mes['user_name']}: {mes['message']}\ntime: {pars_time(mes['data'])}\n")
#         mess = f"{mes['user_name']}: {mes['message']}\ntime: {pars_time(mes['data'])}\n"
#         self.viewMessage.append(mess)


    def pars_time(self, times):
        """ Converts date from 1588759662.14039
            to  May 13:07:42 2020. """
        a = time.ctime(times)
        a = a.split(' ')
        del a[0], a[1]
        a[0], a[1] = a[1], a[0]
        a = ' '.join(a)
        return a





def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Chat()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
