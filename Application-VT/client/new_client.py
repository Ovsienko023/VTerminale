import requests
import json
import time
import sys


HOST = "http://127.0.0.2:5000/"

def get_config():
    try:
        file = open('config.conf')
    except IOError as e:
        # print(u'не удалось открыть файл')
        return {"host": HOST, "login": "_", "password": "_"}
    else:
        # print(u'делаем что-то с файлом')
        with open('config.conf')as r:
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
    def __init__(self):
        self.message = input("Enter message: ")


class RequestServ:
    def __init__(self):
        self.login = User().login
        self.password = User().password
        self.host = get_config()['host']
        self.url_registration = self.host + r'api/v2/registration/'
        self.url_is_login = self.host + r'/api/v2/is_login/'
        self.url_authentication = self.host + f'api/v2/{self.login}/authentication/'
        self.url_is_whom_login = self.host + f'api/v2/{self.login}/is_whom_login/'
        self.url_write_message = self.host + f'api/v2/{self.login}/write_message/'
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

    def check_message(self):
        data = {"password": self.password}
        status = requests.post(self.url_check_message, json=data)
        return status.json()

    def is_login(self, login):
        data = {"login": login}
        status = requests.post(self.url_is_login, json=data)
        return status.json()

user = RequestServ()
status = user.check_message()
print(status)


def main():
    print ('Welcome to Terminal\n')
    user = RequestServ()
    while not user.authentication():
        print('To register, press "0"')
        print('To continue without registration, press "Enter"\n')
        command = input()
        if command == '0':
            print('Registration')
            menu_reg(user)
            
        login = input("Login: ")
        password = input("Password: ")
    User().chenge_user(login, password)
    menu_main(user)


def menu_reg(user):
    while True:
        login = input("Enter login: ")
        if not user.is_login(login):
            password = input("Enter password: ")
            repeat_password = input("Repeat password: ")
            if password == repeat_password:
                User().chenge_user(login, password)
                break    
    status = user.registration(login, password)            
    if status['status']:
        print('You have successfully registered!')


def menu_main(user):
    while True:
        print('\nSelect option: \nTo write message press "1"\nTo check messages press "2"')
        answer = input('\n(enter "q" to exit): ')
        print('----------')
        if answer == '1':
            whom = whom_is(user)
            message = Message()
            status = user.write_message(whom, message)
            print(status)
        if answer == '2':
            data = user.check_message()
            pars_message(data)
        if answer.lower() == 'q':
            break

def whom_is(user):
    whom = input('Enter')
    while not user.is_whom_login():
        whom = input('Enter')
        user.is_whom_login()
    return whom

def pars_message(data):
    for mes in data['messages']:
        print(f"{mes['user_name']}: {mes['message']}\ntime: {pars_time(mes['data'])}\n")
    input("Enter to return")
    print('----------')

def pars_time(times):
    """ converts date from 1588759662.14039 to  May 13:07:42 2020 """
    a = time.ctime(times)
    a = a.split(' ')
    del a[0], a[1]
    a[0], a[1] = a[1], a[0]
    a = ' '.join(a)
    return a

main()
