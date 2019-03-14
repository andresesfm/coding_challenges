import unittest
from binarytree import tree, build, Node
#From https://www.youtube.com/watch?v=13m9ZCB8gjw&index=4&list=PLrmLmBdmIlpuE5GEMDXWf0PWbBD9Ga1lO&t=0s

#__author__ = "Andres Aguilar"

def lowest_common_ancestor(bt,a,b):
    if not bt: 
        return None
    if bt.value == a or bt.value == b:
        return bt
    aa = lowest_common_ancestor(bt.left,a,b)
    bb = lowest_common_ancestor(bt.right,a,b)
    if aa == None and bb == None:
        return None
    if aa == None:
        return bb
    elif bb == None:
        return aa
    return bt


class LCATest(unittest.TestCase):
    def test_1(self):
        values = [3,6,8,2,11,None,13,None,None,9,5,None,None,7,None]
        root = build(values)
        #print(root)
        """
            _______3
           /        \
           6__        8__
           /   \          \
           2     11         13
               /  \       /
               9    5     7
        """
        self.assertEqual(3,lowest_common_ancestor(root,2,8).value)
        self.assertEqual(6,lowest_common_ancestor(root,2,5).value)
        self.assertEqual(11,lowest_common_ancestor(root,9,5).value)
        self.assertEqual(8,lowest_common_ancestor(root,8,7).value)
        self.assertEqual(3,lowest_common_ancestor(root,9,3).value)


if __name__ == "__main__":
    unittest.main()