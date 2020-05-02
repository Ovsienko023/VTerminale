import requests
import json
import time


def status():
    # url = r'http://127.0.0.1:5000/api/v1/info/Bob89'
    user_name = "Bob"
    url = f'http://127.0.0.1:5000/api/v1/{user_name}/check_message'
    data = {"user_name": "Bob", "message": "Hi!"}
    status = requests.post(url, json=data)
    print(status.json())



class Client:
    def __init__(self):
        self.user = User()
    
    def check_message(self):
        user_name = "Bob"
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/check_message'

    def write_message(self):
        user_name = self.user.user_name
        url = f'http://127.0.0.1:5000/api/v1/{user_name}/write_message'
        message = input("Enten messege: ")
        data = {"token": self.user.token, 
                "message":message,
                "data": time.time()}
        self.post(url, data)

    def post(self, url, data):
        status = requests.post(url, json=data)
        # print(status.json())
        return status.json()

    def get(self, url):
        status = requests(url)
        print(status.content)
        return status.content


class User:
    def __init__(self):
        self.user_name = input("Login: ")
        self.token = self.get_token()

    def get_token(self):
        with open('user.conf') as r:
            token = r.readline()
        return token






def main():
    print("Client run!")
    a = Client()
    a.write_message()
    # status()
    

main()
