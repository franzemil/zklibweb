from unittest import TestCase

from zklibweb.domain import Maquine


class MaquineTestCase(TestCase):
    def setUp(self):
        self.maquine = Maquine('0.0.0.0', 'user', 'secret')

    def test_urls(self):
        self.assertEqual(self.maquine.get_host(), 'http://0.0.0.0')
        self.assertEqual(self.maquine.get_url_for_uids(), 'http://0.0.0.0/csl/download?first=0&last=10000')
        self.assertEqual(self.maquine.get_url_for_download(), 'http://0.0.0.0/form/Download')
