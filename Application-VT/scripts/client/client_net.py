import requests
import json
import time


def get_config():
    with open('config.conf')as r:
        data = r.read()
        conf_dict = json.loads(data)
    return conf_dict


class Client:
    def __init__(self):
        self.user = User()
        self.user_name = self.user.name
        self.user_password = self.user.password
        self.url = get_config()['host']

    def check_message(self):
        url = f'{self.url}/api/v1/{self.user_name}/check_message'
        data = {"password": self.user_password}
        status = self.post(url, data)
        return status

    def write_message(self):
        url = f'{self.url}/api/v1/{self.user_name}/write_message'
        while True:
            whom = input("Whom: ")
            if self.is_user(whom):
                break
            print('No user with this name')
            
        message = Message().message
        data = {"password": self.user_password, 
                "message":message,
                "whom": whom,
                "data": time.time()}
        status = self.post(url, data)

    def is_user(self, whom):
        url = f'{self.url}/api/v1/{self.user_name}/is_users'
        data = {"password": self.user_password,
                "whom": whom}
        status = self.post(url, data)
        return status['status']

    def post(self, url, data):
        status = requests.post(url, json=data)
        return status.json()

    def get(self, url):
        status = requests(url)
        return status.content


class User:
    def __init__(self):
        self.name = self.get_name()
        self.password = self.get_password()
        self.url = get_config()['host']
        self.authentication = self.is_authentication()

    def get_name(self):
        name = get_config()['login']
        return name

    def get_password(self):
        password = get_config()['password']
        return password
    
    def is_authentication(self):
        url = f'{self.url}/api/v1/{self.name}/authentication'
        data = {"password": self.password}
        status = requests.post(url, json=data)
        status = status.json()

        while status['status'] == False:
            print("Invalid username or password, try again")
            self.name = input("Login: ")
            self.password = input("Password: ")
            url = f'{self.url}/api/v1/{self.name}/authentication'
            data = {"password": self.password}
            status = requests.post(url, json=data)
            status = status.json()
            print('\n\n')
        self.save_password(self.password)
        return status['status']
    
    def save_password(self, password):
        config = get_config()
        config['password'] = password
        json_config = json.dumps(config)
        with open('config.conf', 'w') as w:
            w.write(json_config)



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
        print("\nSelect option: \nTo write message press '1'\nTo check messages press '2'")
        answer = input('\n(enter "q" to exit): ')
        print('----------')
        if answer == '1':
            client.write_message()
        if answer == '2':
            data = client.check_message()
            message = pars_message(data)
        if answer.lower() == 'q':
            break

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

