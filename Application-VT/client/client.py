import requests
import json
import time
import sys


# HOST = "http://127.0.0.1:5000"

# def get_config():
#     try:
#         file = open('config.conf')
#     except IOError as e:
#         print(u'не удалось открыть файл')
#         return {"host": HOST, "login": "_", "password": "_"}
#     else:
#         print(u'делаем что-то с файлом')
#         with open('config.conf')as r:
#             data = r.read()
#             conf_dict = json.loads(data)
#         return conf_dict


# class color: 
#     PURPLE = '\033[95m' 
#     CYAN = '\033[96m' 
#     DARKCYAN = '\033[36m' 
#     BLUE = '\033[94m' 
#     GREEN = '\033[92m' 
#     YELLOW = '\033[93m' 
#     RED = '\033[91m' 
#     BOLD = '\033[1m' 
#     UNDERLINE = '\033[4m' 
#     END = '\033[0m' 


# class Client:
#     def __init__(self):
#         self.user = User()
#         self.user_name = self.user.name
#         self.user_password = self.user.password
#         self.url = get_config()['host']

#     def check_message(self):
#         url = f'{self.url}/api/v1/{self.user_name}/check_message'
#         data = {"password": self.user_password}
#         status = self.post(url, data)
#         return status

#     def write_message(self):
#         url = f'{self.url}/api/v1/{self.user_name}/write_message'
#         while True:
#             whom = input("Whom: ")
#             if self.is_user(whom):
#                 break
#             print(color.RED + 'No user with this name' + color.END)

#         message = Message().message
#         data = {"password": self.user_password,
#                 "message": message,
#                 "whom": whom,
#                 "data": time.time()}
#         status = self.post(url, data)

#     def save_config(self, conf):
#         with open('config.conf', 'w')as w:
#             json_dict = json.dumps(conf)
#             w.write(json_dict)

#     def is_user(self, whom):
#         url = f'{self.url}/api/v1/{self.user_name}/is_users'
#         data = {"password": self.user_password,
#                 "whom": whom}
#         status = self.post(url, data)
#         return status['status']
    
#     def post(self, url, data):
#         status = requests.post(url, json=data)
#         return status.json()


# class Reg:
#     url_host = get_config()['host']

#     @classmethod
#     def registration(cls):
#         """ Save login and password in config.conf """
#         while True:
#             login = input("Enter login: ")
#             if not cls.is_login(login):
#                 password = input("Enter password: ")
#                 repeat_password = input("Repeat password: ")
#                 if password == repeat_password:
#                     conf = get_config()
#                     cls.save_config(conf)
#                     break     
#         url = f'{cls.url_host}/api/v1/{login}/registration/'
#         data = {"password": password}
#         status = requests.post(url, json=data)
#         status = status.json()
#         if status['status']:
#             print('You have successfully registered!')

#     @classmethod
#     def is_login(cls, login):
#         url = f'{cls.url_host}/api/v1/{login}/is_login'
#         status = requests.post(url, json=None)
#         status = status.json()
#         return status['status']
    
#     @classmethod
#     def save_config(cls, conf):
#         with open('config.conf', 'w')as w:
#             json_dict = json.dumps(conf)
#             w.write(json_dict)
    

# class User:
#     def __init__(self):
#         self.name = self.get_name()
#         self.password = self.get_password()
#         self.url = get_config()['host']
#         self.authentication = self.is_authentication()

#     def get_name(self):
#         name = get_config()['login']
#         return name

#     def get_password(self):
#         password = get_config()['password']
#         return password

#     def is_authentication(self):
#         url = f'{self.url}/api/v1/{self.name}/authentication'
#         data = {"password": self.password}
#         status = requests.post(url, json=data)
#         status = status.json()

#         while not status['status']:
#             print('To register, press "0"')
#             print('To continue without registration, press "Enter"\n')
#             command = input()
#             if command == '0':
#                 print(color.UNDERLINE + 'Registration' + color.END)
#                 Reg.registration()

#             self.name = input("Login: ")
#             self.password = input("Password: ")
#             url = f'{self.url}/api/v1/{self.name}/authentication'
#             data = {"password": self.password}
#             status = requests.post(url, json=data)
#             status = status.json()
#             print('\n\n')
#         self.save_password(self.password, self.name)
#         return status['status']

#     def save_password(self, password, login):
#         config = get_config()
#         config['password'] = password
#         config['login'] = login
#         json_config = json.dumps(config)
#         with open('config.conf', 'w') as w:
#             w.write(json_config)


# class Message:
#     def __init__(self):
#         self.message = input("Enter message: ")

#     def encrypt_message(self):
#         pass

#     def decrypt_message(self):
#         pass



# def main():
#     print (color.UNDERLINE + 'Welcome to Terminal\n' + color.END)
#     client = Client()
    
#     # print('To register, press "0"')
#     # print('To continue without registration, press "Enter"\n')
#     # reg = input('')
#     # print('----------')
#     # if reg == '0':
#     #     client.registration()
#     # client = Client()

#     while True:
#         print('\nSelect option: \nTo write message press "1"\nTo check messages press "2"')
#         answer = input('\n(enter "q" to exit): ')
#         print('----------')
#         if answer == '1':
#             client.write_message()
#         if answer == '2':
#             data = client.check_message()
#             message = pars_message(data)
#         if answer.lower() == 'q':
#             break


# def pars_message(data):
#     for mes in data['messages']:
#         print(f"{mes['user_name']}: {mes['message']}\ntime: {pars_time(mes['data'])}\n")
#     input("Enter to return")
#     print('----------')


# def pars_time(times):
#     """ converts date from 1588759662.14039 to  May 13:07:42 2020 """
#     a = time.ctime(times)
#     a = a.split(' ')
#     del a[0], a[1]
#     a[0], a[1] = a[1], a[0]
#     a = ' '.join(a)
#     return a

# # try:
# #     main()
# # except json.JSONDecodeError:
# #     print(color.RED + 'Restart' + color.END + '\n\n\n')
# #     main()

# def test_url():
#     url = r'http://192.168.16.70:5555/vik'
    
#     a = requests.get(url)
#     print(a.content, '!')
#     cookies = a.cookies
    
#     b = requests.get(url, cookies=cookies)
#     print(b.content, '!!')
#     cookies = b.cookies

#     c = requests.get(url, cookies=cookies)
#     print(c.content, '!!!')

# # test_url()



def registration():
    data = {"password": '123'}
    url = r'http://127.0.0.1:5000/api/v2/bos/registration/'
    status = requests.post(url, json=data)
    return status.json()

def authentication():
    data = {"password": '123'}
    url = r'http://127.0.0.1:5000/api/v2/kik/authentication/'
    status = requests.post(url, json=data)
    return status.json()

def save_message():
    data = {"password": '123',
                "message": 'Hi',
                "whom": 'kik',
                "data": time.time()}
    url = r'http://127.0.0.1:5000/api/v2/kik/write_message/'
    status = requests.post(url, json=data)
    return status.content

def is_whom_login():
    data = {"password": '123',
                "whom": 'kik'}
    url = r'http://127.0.0.1:5000/api/v2/kik/is_whom_login/'
    status = requests.post(url, json=data)
    return status.content

def check_message():
    data = {"password": "123"}
    url = r'http://127.0.0.1:5000/api/v2/kik/check_message/'
    status = requests.post(url)#, json=data)
    return status.content

check_message()
# authentication()
# registration()

    
def menu():
    print (' Welcome to Terminal\n')
    if not authentication()['status']:
        print(registration())
    while True:
        print('\nSelect option: \nTo write message press "1"\nTo check messages press "2"')
        answer = input('\n(enter "q" to exit): ')
        print('----------')
        if answer == '1':
            is_whom_login()
            save_message()
        if answer == '2':
            check_message()
        if answer.lower() == 'q':
            break
# get_config()

# menu()




