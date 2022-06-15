"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTestCase(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 8)
        self.assertEqual(res, 13)
        
    def test_subtract_numbers(self):
        res = calc.sub(5, 8)
        self.assertEqual(res, 3)
