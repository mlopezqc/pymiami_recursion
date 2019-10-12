import unittest
from exercise import count_multiples


class CountMultiples(unittest.TestCase):
    def test_count_4(self):
        self.assertEquals(count_multiples(2, 4), 2)

    def test_count_12(self):
        self.assertEquals(count_multiples(2, 12), 2)

    def test_count_11664(self):
        self.assertEquals(count_multiples(3, 11664), 6)
