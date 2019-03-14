import unittest

#My solution to 
# https://www.youtube.com/watch?v=zGv3hOORxh0

def overlap(rects):
    #first for 2
    r1,r2 = rects
    return ((r1.x1< r2.x1 and r2.x1<r1.x2) and (r1.y1< r2.y1 and r2.y1<r1.y2)) or ((r2.x1< r1.x1 and r1.x1<r2.x2) and (r2.y1< r1.y1 and r1.y1<r2.y2))


class Rect(object):
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class TestOverlap(unittest.TestCase):
    def test_1(self):
        self.assertTrue(overlap([Rect(2,1,5,5),Rect(3,2,5,7)]))

    def test_2(self):
        self.assertFalse(overlap([Rect(0,1,1,0),Rect(2,2,4,4)]))
    
