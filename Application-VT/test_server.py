import unittest
import json
import sys
from scripts.server.server import app
from scripts.logic.utilities import CommandDB


class TestApi(unittest.TestCase):
    def test_registration_1(self):
        """ create 2 new users """      
        test_bob = {"login": "test_bob", "password": "123"}
        test_kik = {"login": "test_kik", "password": "123"}
        x = (test_bob, test_kik)
        for sent in x:
            with app.test_client() as client:
                relult = client.post('api/v2/registration/', json=sent)

    def test_registration_2(self):
        """ json not correct  """
        sent = {"logmn": "bob", "pakword": 123}
        with app.test_client() as client:
            relult = client.post('api/v2/registration/', json=sent)
            self.assertEqual(relult.json, {'info': 'incorrect data',
                                           'status': False})
    
    def test_authentication_1(self):
        """ /authentication/ User is in the system """
        sent = {"password": "123"}
        with app.test_client() as client:
            relult = client.post('/api/v2/test_bob/authentication/', json=sent)
            self.assertEqual(relult.json, {'status': True})
    
    def test_authentication_2(self):
        """ /authentication/ Not user in the system """
        sent = {"password": "123"}
        with app.test_client() as client:
            relult = client.post('/api/v2/nott_bob/authentication/', json=sent)
            self.assertEqual(relult.json, {'status': False}) 

    def test_authentication_3(self):
        """ /authentication/ Not user in the system """
        sent = {"pakword": "123"}
        with app.test_client() as client:
            relult = client.post('/api/v2/nott_bob/authentication/', json=sent)
            self.assertEqual(relult.json, {'info': 'incorrect data',
                                           'status': False}) 

    def test_is_login_1(self):
        """ /is_login/ If login is in DB """
        with app.test_client() as client:
            sent = {"login": 'test_kik'}
            relult = client.post('/api/v2/is_login/', json=sent)
            self.assertEqual(relult.json, {'status': True})
            
    
    def test_is_login_2(self):
        """ /is_login/ If login is not in DB """
        with app.test_client() as client:
            sent = {"login": 'notlogin'}
            relult = client.post('/api/v2/is_login/', json=sent)
            self.assertEqual(relult.json, {'status': False})
    
    def test_is_login_3(self):
        """ /is_login/ If json is not correct """
        with app.test_client() as client:
            sent = {"abrktl": 'notlogin'}
            relult = client.post('/api/v2/is_login/', json=sent)
            self.assertEqual(relult.json, {'info': 'incorrect data',
                                           'status': False})

    def test_is_login_4(self):
        """ /is_login/ Use get instead post  """
        with app.test_client() as client:
            relult = client.get('/api/v2/is_login/')
            self.assertEqual(relult.json, None)

    def test_write_message_1(self):
        """ /write_message/ Save massage in BD  
            valid json """
        sent = {"password": "123",
                "message": "Hi kik!",
                "whom": "test_kik",
                "data": 1589871051.0788183}
        with app.test_client() as client:
            relult = client.post('/api/v2/test_bob/write_message/', json=sent)
            self.assertEqual(relult.json, {'status': True})

    def test_write_message_2(self):
        """ /write_message/ Save massage in BD  
            not valid json """
        sent = {"not_password": "123",
                "message": "Hi kik!",
                "not_whom": "test_kik",
                "data": 1589871051.0788183}
        with app.test_client() as client:
            relult = client.post('/api/v2/test_bob/write_message/', json=sent)
            self.assertEqual(relult.json, {"status": False,
                                           "info": "incorrect json"})

    def test_write_message_3(self):
        """ /write_message/ Save massage in BD  
            not valid json(time) """    
        test_time_1 = {"password": "123",
                        "message": "Hi kik!",
                        "whom": "test_kik",
                        "data": "1589871051.0788183"}
        test_time_2 = {"password": "123",
                        "message": "Hi kik!",
                        "whom": "test_kik",
                        "data": 15898710510788183}
        test_time_3 = {"password": "123",
                        "message": "Hi kik!",
                        "whom": "test_kik",
                        "data": [1,2,3]}
        
        x = (test_time_1, test_time_2, test_time_3)
        for sent in x:
            with app.test_client() as client:
                relult = client.post('/api/v2/test_bob/write_message/', json=sent)
                with self.subTest(sent):
                    self.assertEqual(relult.json, {"status": False,
                                                    "info": "incorrect json (time)"})

    def test_is_whom_1(self):
        """ /is_whom_login/ If user in DB"""
        with app.test_client() as client:
            sent = {"password": "123",
                    "whom": 'test_kik'}
            relult = client.post('/api/v2/test_bob/is_whom_login/', json=sent)
            self.assertEqual(relult.json, {"status": True})

    def test_is_whom_2(self):
        """ /is_whom_login/ If user in not DB"""
        with app.test_client() as client:
            sent = {"password": "123",
                    "whom": 'not_test_kik'}
            relult = client.post('/api/v2/test_bob/is_whom_login/', json=sent)
            self.assertEqual(relult.json, {"status": False})
    
    def test_is_whom_3(self):
        """ /is_whom_login/ If json not correct """
        with app.test_client() as client:
            sent = {"not_password": "123",
                    "whom": 'not_test_kik'}
            relult = client.post('/api/v2/test_bob/is_whom_login/', json=sent)
            self.assertEqual(relult.json, {"status": False,
                                           "info": "incorrect data"})

    def test_check_message_1(self):
        """ /check_message/ for urser """
        with app.test_client() as client:
            sent = {"password": "123"}
            relult = client.post('/api/v2/test_kik/check_message/', json=sent)
            self.assertEqual(relult.json, {"status": True, 'counter': 1})
    
    def test_check_message_2(self):
        """ /check_message/ for urser """
        with app.test_client() as client:
            sent = {"not_password": '123'}
            relult = client.post('/api/v2/test_kik/check_message/', json=sent)
            self.assertEqual(relult.json, {"status": False, "info": "incorrect json"})

    def test_read_message_1(self):
        """ /read_message/ for urser """
        with app.test_client() as client:
            sent = {"password": "123"}
            relult = client.post('/api/v2/test_kik/read_message/', json=sent)
            self.assertEqual(relult.json['status'],  True)

    def test_read_message_2(self):
        """ /read_message/ for urser no correct password """
        with app.test_client() as client:
            sent = {"password": ["not123"]}
            relult = client.post('/api/v2/test_kik/read_message/', json=sent)
            self.assertEqual(relult.json,  {"status": False})
            

def test_server_run():
    unittest.main()

test_server_run()