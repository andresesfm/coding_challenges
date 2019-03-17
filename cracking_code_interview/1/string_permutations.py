import unittest
from collections import Counter

def is_permutation(s1,s2):
    return Counter(s1) == Counter(s2)


class TestCheckPermutation(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_permutation("",""))

    def test_single(self):
        self.assertFalse(is_permutation("","A"))

    def test_true(self):
        self.assertTrue(is_permutation("AB","BA"))

if __name__ == "__main__":
    unittest.main()
