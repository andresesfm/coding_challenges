import unittest
from collections import Counter

def sortO(s: str) -> str:
    c = Counter(s)
    b = sorted(c.items(), key=lambda kv: kv[1], reverse=True)
    print(b)
    return "".join([i[0] for i in b])

class TestSortO(unittest.TestCase):
    def test_provided(self):
        self.assertEqual('tbjy',sortO('bbbttyjjjtt'))


if __name__ == "__main__":
    unittest.main()