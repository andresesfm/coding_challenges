import unittest
from collections import Counter
import copy

#Implements all string permutations. Question by Tushar here: https://www.youtube.com/watch?v=nYFd7VHKyWQ
def permutations(s):
    alpha = Counter(s)
    per = permutationsDict("",alpha)
    return per

def permutationsDict(p,d):
    a = []
    done = True
    for e in d:
        if d[e] >0: 
            done = False 
            nd = copy.deepcopy((d))
            nd[e] = nd[e]-1 
            a = a + permutationsDict(p + e, nd)
    if done:
        a = a+[p]
    return a


class PermutationsTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([''],permutations(""))

    def test_single(self):
        self.assertEqual(["A"],permutations("A"))

    def test_double(self):
        self.assertEqual(["Ab","bA"],permutations("Ab"))

    def test_triple_dup(self):
        self.assertEqual(['AAb', 'AbA', 'bAA'],permutations("AAb"))

    def test_video_example(self):
        self.assertEqual([ 'AABC', 'AACB',  'ABAC','ABCA', 'ACAB',  'ACBA', 'BAAC', 'BACA', 'BCAA', 'CAAB',  'CABA', 'CBAA'],permutations("AABC"))