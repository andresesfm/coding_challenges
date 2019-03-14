import unittest
import math
from heapq import heappush, heappop

#Takes array or tuples and returns an array with the closest k elements to the origin
# https://www.youtube.com/watch?v=eaYX0Ee0Kcg

class Coordinate(object):
    def __init__(self,p):
        self.x, self.y = p
    
    def __lt__(self, value):
        return math.sqrt(self.x**2+self.y**2)<math.sqrt(value.x**2+value.y**2)
    def to_tuple(self):
        return (self.x,self.y)

def closest(arr,k):
    hp = []
    for e in arr:
        heappush(hp,Coordinate(e))
    return [ heappop(hp).to_tuple() for i in range(min(k,len(hp))) ]

class TestKclosest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([(0,1)],closest([(0,1)],1))

    def test_2(self):
        self.assertEqual([(0,1)],closest([(0,1),(2,2)],1))

    def test_3(self):
        self.assertEqual([(0,1),(2,2)],closest([(0,1),(2,2)],2))

    def test_4(self):
        self.assertEqual([(0,1),(2,2)],closest([(0,1),(2,2)],4))
    
    def test_5(self):
        self.assertEqual([(0,1),(2,2)],closest([(5,5),(2,2),(0,1)],2))

    def test_dojo(self):
        self.assertEqual(set([(0, -2),(-1, 0)]),set(closest([(-2,-4),(0,-2),(-1,0),(3,-5),(-2,-3,),(3,2)],2)))

if __name__ == '__main__':
    unittest.main()
