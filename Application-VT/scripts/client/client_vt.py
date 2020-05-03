import requests
import json
import time


class Client:
    def __init__(self):
        self.user = User()
    
    def check_message(self):
        user_name = "Bob"
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/check_message'

    def write_message(self):
        user_name = self.user.user_name
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/write_message'
        message = Message().message
        data = {"password": self.user.password, 
                "message":message,
                "data": time.time()}
        self.post(url, data)

    def post(self, url, data):
        status = requests.post(url, json=data)
        return status.json()

    def get(self, url):
        status = requests(url)
        print(status.content)
        return status.content


class User:
    def __init__(self):
        self.user_name = input("Login: ")
        self.password = self.get_tpassword()

    def get_password(self):
        with open('user.conf') as r:
            password = r.readline()
        return password

class Message:
    def __init__(self):
        self.message = input("Enter message: ")

    def encrypt_message(self):
        pass

    def decrypt_message(self):
        pass






def status():
    user_name = "Bob"
    url = f'http://127.0.0.1:5000/api/v1/{user_name}/check_message'
    data = {"user_name": "Bob", "message": "Hi!"}
    status = requests.post(url, json=data)
    print(status.json())

def main():
    print("Client run!")
    a = Client()
    a.write_message()
    # status()
    

main()


