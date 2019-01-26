import unittest
import requests

class logintest(unittest.TestCase):
    def testlogin(self):
        url = "http://xx/login.html"
        form = {"username":123}
        r = requests.post(url, data = form)
        self.assertEqual(r.text, "login success")