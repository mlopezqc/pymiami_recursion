import unittest
from exercise_mlopezqc import count_multiples


class CountMultiples(unittest.TestCase):
    def test_count_1(self):
        self.assertEquals(count_multiples(2, 4), 2)

    def test_count_2(self):
        self.assertEquals(count_multiples(2, 12), 2)

    def test_count_3(self):
        self.assertEquals(count_multiples(3, 11664), 6)
