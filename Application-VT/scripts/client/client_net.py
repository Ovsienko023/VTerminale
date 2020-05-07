import requests
import json
import time


class Client:
    def __init__(self):
        self.user = User()
        self.user_name = self.user.name
        self.user_password = self.user.password

    def check_message(self):
        user_name = self.user_name
        url = f'https://00500421.ngrok.io/api/v1/{user_name}/check_message'
        data = {"password": self.user_password}
        status = self.post(url, data)
        return status

    def write_message(self):
        user_name = self.user_name
        url = f'https://00500421.ngrok.io/api/v1/{user_name}/write_message'
        message = Message().message
        data = {"password": self.user_password, 
                "message":message,
                "whom": input("Whom: "),
                "data": time.time()}
        status = self.post(url, data)
        # print(status)


    def post(self, url, data):
        status = requests.post(url, json=data)
        return status.json()

    def get(self, url):
        status = requests(url)
        print(status.content)
        return status.content


class User:
    def __init__(self):
        self.name = input("Login: ")
        self.password = self.get_password()
        self.authentication = self.is_authentication()

    def get_password(self):
        with open('user.conf') as r:
            password = r.readline()
        return password
    
    def is_authentication(self):
        url = f'https://00500421.ngrok.io/api/v1/{self.name}/authentication'
        data = {"password": self.password}
        status = requests.post(url, json=data)
        status = status.json()

        while status['status'] == False:
            print("Неправильный логин или пароль, попробуйте снова")
            self.name = input("Login: ")
            self.password = input("Password: ")
            url = f'https://00500421.ngrok.io/api/v1/{self.name}/authentication'
            data = {"password": self.password}
            status = requests.post(url, json=data)
            status = status.json()
            print('\n\n')
        self.save_password(self.password)
        return status['status']
    
    def save_password(self, password):
        with open('user.conf', 'w') as w:
            w.write(password)


class Message:
    def __init__(self):
        self.message = input("Enter message: ")

    def encrypt_message(self):
        pass

    def decrypt_message(self):
        pass




def main():
    print("Welcome to Terminal\n")
    client = Client()
    
    while True:
        print("\nSelect option: \n1) To write a message\n2) To check a messages")
        answer = input('\n(enter "q" to exit): ')
        print('----------')
        if answer == '1':
            client.write_message()
        if answer == '2':
            data = client.check_message()
            message = pars_message(data)
        if answer.lower() == 'q':
            break
    
    # print(data, type(data))
    # mess = f"You have {len(data)} new message"
    # print(mess)
    # print('New message!')
    # print(f"{data['user_name']}: {data['message']}\ntime: {time.ctime(data['data'])}")
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

# url = r'https://00500421.ngrok.io/api/v1/info/bob'
# data = {"password": '123'}
# status = requests.post(url, json=data)
# print(status.json())

#____---------------____
#To write message press "1"