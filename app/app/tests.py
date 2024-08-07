"""
Sample test for calc module about sum of 2 numbers
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtruct(self):

        res = calc.subtruct(10, 15)
        self.assertEqual(res, 5)


