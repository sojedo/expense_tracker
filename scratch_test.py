import unittest

def double(n):
    return n * 2

class TestDouble(unittest.TestCase):
    def test_three(self):
        self.assertEqual(double(3), 6)

    def test_zero(self):
        self.assertEqual(double(0), 0)