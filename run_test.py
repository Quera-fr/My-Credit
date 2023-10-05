import unittest
from run import r
from fastapi.testclient import TestClient


class TestFunctions(unittest.TestCase):

    def test_r(self):
        self.assertEqual(r(2), 1)

class TestAPI(unittest.TestCase):

    def test_test(self):
        self.assertEqual(1, 1)
