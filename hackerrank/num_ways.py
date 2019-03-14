import unittest

"""
https://www.youtube.com/watch?v=qli-JCrSwuk
"""

def num_ways(s):
    if len(s) == 0:
        return 0
    elif s[0] == '0':
        return 0
    elif len(s) == 1:
        return 1
    
    nw =  num_ways(s[1:])
    print(f'nw1={nw} + {s[1]} + {s[1:3]}')
    if int(s[1:3]) >9 and int(s[1:3])<27:
        nw += num_ways(s[2:])
        print(f'nw2={nw}')
    return nw

class NumWays(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(0,num_ways(""))

    def test_11(self):
        self.assertEqual(2,num_ways("123"))
    def test_12(self):
        self.assertEqual(1,num_ways("456"))
    def test_13(self):
        self.assertEqual(3,num_ways("111"))


if __name__ == '__main__':
    unittest.main()