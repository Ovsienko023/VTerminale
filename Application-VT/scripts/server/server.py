from flask import Flask, request
from scripts.logic.utilities import AuthenticationError
from scripts.logic.utilities import Destributor
from scripts.logic.utilities import WrapperDB
import json


app = Flask(__name__)


@app.route('/api/v2/registration/', methods=['POST'])
def registration():
    data = request.json
    login = data['login']
    password = data['password']
    user = Destributor(login, password)
    status = user.registration()
    return {"status": status}


@app.route('/api/v2/<login>/authentication/', methods=['POST'])
def authentication(login):
    """ Сравнивает логин и пароль пользователя с БД """
    print(login)
    data = request.json
    print(data)
    password = data['password']
    user = Destributor(login, password)
    if user.authentication:
        return {'status': True}
    return {'status': False}


@app.route('/api/v2/is_login/', methods=['POST'])
def is_login():
    data = request.json
    print(data)
    login = data['login']
    user = Destributor(login, '-')
    status = user.is_user()
    return {"status": status}


@app.route('/api/v2/<login>/is_whom_login/', methods=['POST'])
def is_whom_login(login):
    data = request.json
    print(data)
    password = data['password']
    if user.authentication:
        user = Destributor(login, password, data=data)
        status = user.is_whom_user(data)
        return {"status": status}


@app.route('/api/v2/<login>/write_message/', methods=['POST'])
def write_message(login):
    print(login)
    data = request.json
    print(data)
    password = data['password']
    user = Destributor(login, password, data)
    if user.authentication:
        status = user.seve_message(data)
        return {"status": status}
    return {"status": False}


@app.route('/api/v2/<login>/check_message/', methods=['POST'])
def check_message(login):
    print(login)
    data = request.json
    print(data)
    password = data['password']
    user = Destributor(login, password)
    if user.authentication:
        status = user.check_message()
        print(status)
        if status['messages']:
            return status
        status['status'] = False
        return status
    return {"status": False}
