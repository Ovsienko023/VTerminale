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
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/check_message'
        data = {"password": self.user_password}
        status = self.post(url, data)
        if status:
            return status
        else:
            return status.content

    def write_message(self):
        user_name = self.user_name
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/write_message'
        message = Message().message
        data = {"password": self.user_password, 
                "message":message,
                "whom": input("Whom: "),
                "data": time.time()}
        status = self.post(url, data)
        print(status.content)


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
        url = f'http://127.0.0.1:5000/api/v1/{self.name}/authentication'
        data = {"password": self.password}
        status = requests.post(url, json=data)
        status = status.json()

        while status['status'] == False:
            print("Неправильный логин или пароль, попробуйте снова")
            self.name = input("Login: ")
            self.password = input("Password: ")
            url = f'http://127.0.0.1:5000/api/v1/{self.name}/authentication'
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
    print("Client run!")
    a = Client()
    # a.write_message()
    data = a.check_message()
    # print(data, type(data))
    print('New message!')
    print(f"{data['user_name']}: {data['message']}\ntime: {time.ctime(data['data'])}")
    

main()


