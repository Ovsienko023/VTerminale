import sys
from PyQt5 import QtWidgets
import chat_v1
import requests
import json
import time
import sys
import os
import login_in


HOST = "http://192.168.16.70:5555/"


def get_config():
    path = os.getcwd() + "/config.json"
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
        print('!!!!!!!!!!')
        conf = get_config()
        conf['login'] = login
        conf['password'] = password
        with open('config.json', 'w') as w:
            json_dict = json.dumps(conf)
            print(json_dict)
            w.write(json_dict)


class Message:
    def __init__(self, message):
        self.message = message


class RequestServ:
    def __init__(self):
        self.login = User().login
        self.password = User().password
        self.host = get_config()['host']
    
    def url_registration(self):
        return self.host + r'api/v2/registration/'

    def url_is_login(self):
        return self.host + r'api/v2/is_login/'

    def url_authentication(self):
        return self.host + f'api/v2/{self.login}/authentication/'

    def url_is_whom_login(self):
        return self.host + f'api/v2/{self.login}/is_whom_login/'

    def url_write_message(self):
        return self.host + f'api/v2/{self.login}/write_message/'

    def url_read_message(self):
        return self.host + f'api/v2/{self.login}/read_message/'

    def url_check_message(self):
        return self.host + f'api/v2/{self.login}/check_message/'
    
    def url_get_friends(self):
        return self.host + f'/api/v2/{self.login}/get_friends/'

    def registration(self, login, password) -> dict:
        data = {"login": login,
                "password": password}
        status = requests.post(self.url_registration(), json=data)
        return status.json()

    def authentication(self):
        data = {"password": self.password}
        status = requests.post(self.url_authentication(), json=data)
        return status.json()

    def is_whom_login(self, whom):
        data = {"password": self.password,
                "whom": whom}
        status = requests.post(self.url_is_whom_login(), json=data)
        return status.json()

    def write_message(self, whom, message):
        print(self.password, self.login)
        data = {"password": self.password,
                "message": message,
                "whom": whom,
                "data": time.time()}
        status = requests.post(self.url_write_message(), json=data)
        return status.json()

    def read_message(self):
        data = {"password": self.password}
        status = requests.post(self.url_read_message(), json=data)
        return status.json()

    def check_message(self):
        data = {"password": self.password}
        status = requests.post(self.url_check_message(), json=data)
        return status.json()

    def is_login(self, login):
        data = {"login": login}
        status = requests.post(self.url_is_login(), json=data)
        return status.json()
    
    def get_friends(self):
        data = {"password": self.password}
        status = requests.post(self.url_get_friends(), json=data)
        return status.json()


class Chat(QtWidgets.QMainWindow, chat_v1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        users = list()  # create list friends
        users.append('')
        users = users + RequestServ().get_friends()['friends']
        self.comboBox.addItems(users)
        self.pushButton.clicked.connect(self.send_message)
        self.pushButton_2.clicked.connect(self.read_message)
        
    def send_message(self):
        print('Нажатие на кнопку Send')
        text_message = self.writeMessage.toPlainText()
        num_lst = self.comboBox.view().currentIndex().row()
        whom = self.comboBox.itemText(num_lst)

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

    def pars_time(self, times):
        """ Converts date from 1588759662.14039
            to  May 13:07:42 2020. """
        a = time.ctime(times)
        a = a.split(' ')
        del a[0], a[1]
        a[0], a[1] = a[1], a[0]
        a = ' '.join(a)
        return a


class Login(QtWidgets.QMainWindow, login_in.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginInPushButton.clicked.connect(self.log_in)
        
    def log_in(self):
        print('Button Login in')
        login = self.LoginLineEdit.text()
        password = self.passwordLineEdit.text()
        user = RequestServ()
        user.login = login
        user.password = password
        status = user.authentication()

        print(login, password, status)
        if status['status']:
            User().chenge_user(login, password)
            self.close()
        
    




def widget_login():
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


def main():
    widget_login()
    app = QtWidgets.QApplication(sys.argv)
    window = Chat()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
