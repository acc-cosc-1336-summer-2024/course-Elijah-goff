import unittest
from src.examples.a_example.devprocess import add_numbers
from src.examples.a_example.devprocess import subtract_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))


    def test_subtract_numbers_1(self):
        self.assertEqual(3, subtract_numbers(6, 3))
        self.assertEqual(9, subtract_numbers(12, 3))
        self.assertEqual(7, subtract_numbers(10, 3))
    

