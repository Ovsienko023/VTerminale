from flask import Flask, request
from flask import render_template
from flask_cors import CORS
from scripts.logic.utilities import AuthenticationError
from scripts.logic.utilities import Destributor
from scripts.logic.utilities import WrapperDB
from scripts.logic.utilities import validator_time
import json


app = Flask(__name__)
CORS(app)


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


@app.route('/api/v2/<login>/get_friends/', methods=['POST'])
def get_friends(login):
    print('get_friends')
    try:
        data = request.json
        print(data)
        password = data['password']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, password)
    if user.authentication:
        user = Destributor(login, password, data=data)
        lst_friends = user.get_friends()
        return {"status": True, "friends": lst_friends}
    return {"status": False}


@app.route('/api/v2/<login>/is_friend/', methods=['POST'])
def is_friend(login):
    try:
        data = request.json
        print(data)
        password = data['password']
        friend = data['friend']
    except KeyError:
        return {"status": False, "info": "incorrect data"}
    user = Destributor(login, password)
    if user.authentication:
        user = Destributor(login, password, data=data)
        status = user.is_friend(login, friend)
        return {"status": status}
    return {"status": False}


@app.route('/api/v2/web_registration/', methods=['GET', 'POST'])
def web_registration():
    print(request.json)
    # try:
    #     data = request.json
    #     login = data['login']
    #     password = data['password']
    # except KeyError:
    #     return {"status": False, "info": "incorrect data"}
    # user = Destributor(login, password)
    # status = user.registration()
    return render_template('index.html')
