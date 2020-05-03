from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/api/v1/info/<user_name>', methods=['GET'])
def info(user_name):
    # data = request.json
    print(user_name)
    return {"ok": True}

@app.route('/api/v1/<user_name>/check_message', methods=['POST'])
def check_message(user_name):
    print(user_name)
    data = request.json
    # print(data)
    return {"ok check message": True}


@app.route('/api/v1/<user_name>/write_message/', methods=['POST'])
def write_message(user_name):
    print(user_name)
    data = request.json
    print(data)
    return {"ok write message": True}

@app.route('/api/v1/<user_name>/authentication/', methods=['POST'])
def authentication(user_name):
    """ Сравнивает логин и пароль пользователя с БД """
    pass

@app.route('/api/v1/<user_name>/registration/', methods=['POST'])
def registration(user_name):
    """ Проверяет есть ли такой Логин и если нет, создаёт password и отправляет его пользователю """
    pass
# registration
