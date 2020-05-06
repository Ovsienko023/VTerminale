# from scripts.logic.utilities import WrapperDB
# from scripts.logic.utilities import AuthenticationError

# def main_logic(user_name, data, command):
#     print('main logic:')
#     password = data['password']
#     try:
#         client = WrapperDB(user_name, password)
#     except AuthenticationError:
#         return False

#     if command == 'write_message':
#         doc = dict()
#         doc["user_name"] = user_name
#         doc["whom"] = data["whom"]
#         doc["data"] = data["data"]
#         doc["message"] = data["message"]
#         doc["status"] = "not_view"
#         client.seve_message(doc)
#         return True
