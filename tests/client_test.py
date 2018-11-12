from unittest import TestCase
from datetime import datetime as dt

from zklibweb.client import ZkMaquine
from zklibweb.domain import Maquine
from zklibweb.exceptions import ZklibWebNetworkException

class ClientTestCase(TestCase):
    def setUp(self):
        self.maquine = Maquine('192.18.241.9', 'user', 'secret')
        self.client = ZkMaquine(self.maquine)

    def test_client_login(self):
        self.assertEqual(self.client.login(), True, 'Error trying login')

    def test_get_uids(self):
        self.client.login()
        self.assertTrue(isinstance(self.client.get_uids(), list), 'It should return a items')

    def test_get_data(self):
        self.client.login()
        self.assertTrue(isinstance(self.client.get_data(dt.now(), dt.now()), list))

    def tearDown(self):
        self.client.close()


class ClientWithBadCredencialTestCase(TestCase):
    def setUp(self):
        self.maquine_two = Maquine('192.1.21.9', 'user', 'secret')
        self.client = ZkMaquine(self.maquine_two)

    def test_client_login(self):
        self.assertEqual(self.client.login(), False, 'Invalid login with bad credencials')

    def test_get_uids(self):
        with self.assertRaises(ValueError):
            self.client.get_uids()

    def tearDown(self):
        self.client.close()

class ClientServerInvalidTestCase(TestCase):
    def setUp(self):
        self.maquine_two = Maquine('292.16.21.9', 'user', 'secret')
        self.client = ZkMaquine(self.maquine_two)

    def test_client_login(self):
        with self.assertRaises(ZklibWebNetworkException):
            self.client.login()

    def tearDown(self):
        self.client.close()
