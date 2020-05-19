from flask import Flask, request
from scripts.logic.utilities import AuthenticationError
from scripts.logic.utilities import Destributor
from scripts.logic.utilities import WrapperDB
from scripts.logic.utilities import validator_time
import json


app = Flask(__name__)


@app.route('/api/v2/registration/', methods=['POST'])
def registration():
    try:
        data = request.json
        login = data['login']
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, password)
    status = user.registration()
    return {"status": status}


@app.route('/api/v2/<login>/authentication/', methods=['POST'])
def authentication(login):
    try:
        print(login)
        data = request.json
        print(data)
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, password)
    if user.authentication:
        return {'status': True}
    return {'status': False}


@app.route('/api/v2/is_login/', methods=['POST'])
def is_login():
    try:
        data = request.json
        print(data)
        login = data['login']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, '-')
    status = user.is_user()
    return {"status": status}


@app.route('/api/v2/<login>/is_whom_login/', methods=['POST'])
def is_whom_login(login):
    try:
        data = request.json
        print(data)
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, password)
    if user.authentication:
        user = Destributor(login, password, data=data)
        status = user.is_whom_user(data)
        return {"status": status}


@app.route('/api/v2/<login>/write_message/', methods=['POST'])
def write_message(login):
    try:
        print(login)
        data = request.json
        print(data)
        password = data['password']
        validator_time(data)
    except KeyError:
        return {"status": False, "info": "incorrect json"}
    except (OSError, TypeError):
        return {"status": False, "info": "incorrect json (time)"}
    user = Destributor(login, password, data)
    if user.authentication:
        status = user.seve_message(data)
        return {"status": status}
    return {"status": False}


@app.route('/api/v2/<login>/read_message/', methods=['POST'])
def read_message(login):
    try:
        print(login)
        data = request.json
        print(data)
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect json"}
    user = Destributor(login, password)
    if user.authentication:
        status = user.read_message()
        print(status)
        if status['messages']:
            return status
        status['status'] = False
        return status
    return {"status": False}


@app.route('/api/v2/<login>/check_message/', methods=['POST'])
def check_message(login):
    try:
        print(login)
        data = request.json
        print(data)
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect json"}
    user = Destributor(login, password)
    if user.authentication:
        counter = user.check_message()
        return{"status": True,
               "counter": counter}
    return {"status": False,
            "counter": 0}
