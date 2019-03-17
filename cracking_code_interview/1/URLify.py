import unittest
from collections import Counter

def URLify(s,l):
    res = []
    for i in range(l):
        if s[i] == ' ':
            res.append('%20')
        else:
            res.append(s[i])
    return ''.join(res)



class TestURLify(unittest.TestCase):
    def test_example(self):
        self.assertEqual("Mr%20John%20Smith",URLify("Mr John Smith    ",13))

if __name__ == "__main__":
    unittest.main()
