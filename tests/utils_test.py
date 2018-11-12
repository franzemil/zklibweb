from unittest import TestCase

from zklibweb.utils import raw_data


class UtilsTestCase(TestCase):
    def test_raw_data(self):
        data = open('./tests/data.dat', 'r').read()
        self.assertEqual(len(raw_data(data)), 3)
