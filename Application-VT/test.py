import unittest
# import requests
import json
import sys
from scripts.server.server import app

class TestApi(unittest.TestCase):

    def test_registration_1(self):
        """ create 2 new users """      
        test_bob = {"login": "test_bob", "password": "123"}
        test_kik = {"login": "test_kik", "password": "123"}
        x = (test_bob, test_kik)
        for sent in x:
            with app.test_client() as client:
                relult = client.post('api/v2/registration/', json=sent)
                with self.subTest(sent):
                    self.assertEqual(relult.json, {'status': True})

    def test_registration_2(self):
        """ json not correct  """
        sent = {"logmn": "bob", "pakword": 123}
        with app.test_client() as client:
            relult = client.post('api/v2/registration/', json=sent)
            self.assertEqual(relult.json, {'info': 'incorrect data',
                                           'status': False})

                                
    # def test_is_login_1(self):
    #     """ /is_login/ If login is in DB """
    #     with app.test_client() as client:
    #         sent = {"login": 'kik'}
    #         relult = client.post('/api/v2/is_login/', json=sent)
    #         self.assertEqual(relult.json, {'status': True})
    
    # def test_is_login_2(self):
    #     """ /is_login/ If login is not in DB """
    #     with app.test_client() as client:
    #         sent = {"login": 'notlogin'}
    #         relult = client.post('/api/v2/is_login/', json=sent)
    #         self.assertEqual(relult.json, {'status': False})
    
    # def test_is_login_3(self):
    #     """ /is_login/ If json is not correct """
    #     with app.test_client() as client:
    #         sent = {"abrktl": 'notlogin'}
    #         relult = client.post('/api/v2/is_login/', json=sent)
    #         self.assertEqual(relult.json, {'info': 'incorrect data',
    #                                        'status': False})
            
    # def test_is_login_4(self):
    #     """ /is_login/ Use get instead post  """
    #     with app.test_client() as client:
    #         relult = client.get('/api/v2/is_login/')
    #         print(relult.json)
    #         self.assertEqual(relult.json, None)

    # def test_is_whom_1(self):
    #     with app.test_client() as client:
    #         sent = {"password": "123",
    #                 "whom": 'bob'}
    #         relult = client.get('/api/v2/kik/is_whom_login/', json=sent)
    #         print(relult.json, '!')


if __name__ == '__main__':
    unittest.main()
