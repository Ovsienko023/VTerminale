import sys
sys.path[0] = sys.path[0][:-8]
from scripts.logic.utilities import ConnectDB


def creat_db():
    db = ConnectDB().db
    coll_message = db['message']
    coll_users = db['users']

creat_db()
