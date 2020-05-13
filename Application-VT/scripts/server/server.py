from flask import Flask, request
from scripts.logic.utilities import AuthenticationError
from scripts.logic.utilities import Destributor
import json


app = Flask(__name__)


@app.route('/api/v2/<login>/registration/', methods=['POST'])
def registration(login):
    data = request.json
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


@app.route('/api/v2/<login>/is_whom_login/', methods=['POST'])
def is_whom_login(login):
    data = request.json
    print(data)
    password = data['password']
    user = Destributor(login, password, data=data)
    status = user.is_whom_user()
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
        return {'status': status}
    return {"ok write message": True}



@app.route('/api/v2/<login>/check_message', methods=['POST'])
def check_message(login):
    print(login)
    data = request.json
    print(data, '!')
    return True
    # password = data['password']
    # user = Destributor(login, password)
    # status = user.check_message()
    # print(status)
    # if status:
    #     # print(status, type(status))
    #     # print(type()
    #     return status
    # return {}




###### ДУБЛИРОВАНИЕ

###### ДУБЛИРОВАНИЕ

# @app.route('/api/v1/<user_name>/is_login', methods=['POST'])
# def is_login(user_name):
#     print(user_name)
#     data = request.json
#     print(data)
#     status = WrapperDB.is_login(user_name)
#     return {"status": status}

# app.run()
# # 'https://stackoverflow.com/questions/54992412/flask-login-usermixin-class-with-a-mongodb'




# from flask import Flask, session

# app = Flask(__name__)
# app.secret_key = 'app secret key'

# print(app.config['SECRET_KEY'])
# for i in app.config:
#     print(i)
# @app.route('/<login>')
# def index(login):
#     if 'counter' in session:
#             session['counter'] += 1
#     else:
#         session['counter'] = 1
    
#     # session.pop('login', None)
#     # session.pop('counter', None)
    
#     return {"st": session['counter']}


# app.run(host='192.168.16.70', port=5555)
