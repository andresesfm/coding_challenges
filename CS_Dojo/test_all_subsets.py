import unittest
import copy

# Code challenge to find all subsets given an array. Posed here: https://www.youtube.com/watch?v=bGC2fNALbNU&t=48s
# Fixed solution posted here: https://stackoverflow.com/a/54812412/570612
def all_subsets(arr):
    subs = [[]]
    for e in arr:
        sub = copy.deepcopy(subs)
        for k in subs:
            k.append(e)
        subs.extend(sub)
    return subs
        


class TestAllSubsets(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual([[]],all_subsets([]))

    def test_1(self):
        self.assertEqual([[1],[]],all_subsets([1]))

    def test_2(self):
        self.assertEqual([[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1],[]],all_subsets([1,2,3]))

if __name__ == '__main__':
    unittest.main()