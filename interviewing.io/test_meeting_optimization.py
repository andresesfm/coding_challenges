import unittest
from typing import List

class Sched(object):
    def __init__(self, length, name):
        self.length = length
        self.name = name

"""
Maximizing number of meetings one can attend given a time limit 
Solves: https://www.youtube.com/watch?v=Q5_2BCej9hg&t=813s
"""
def canAttend(requested: List[Sched], hours: int) -> List[Sched]: 
    if not requested or hours <=0:
        return []
    s = requested[0]
    if s.length > hours:
        return canAttend(requested[1:], hours)
    else:
        included = [s]
        included.extend(canAttend(requested[1:],hours-s.length))
        excluded = canAttend(requested[1:],hours)
        if len(included)> len(excluded):
            return included
        else:
            return excluded


class TestCanAttend(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([],canAttend([],3))
        self.assertEqual([],canAttend([Sched(1,1)],0))

    def test_provided(self):
        s1 = Sched(1,1)
        self.assertEqual([s1],canAttend([s1],1))


if __name__ == "__main__":
    unittest.main()