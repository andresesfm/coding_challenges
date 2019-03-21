import unittest

# Do strings match with up to k edits/deletes?
def equals_edit(s1,s2, k):
    l1 = len(s1)
    l2 = len(s2)

    if l1 == 0 and l2 == 0:
        return True
    
    if (l1 == 0 or l2 ==0) and k <=0:
        return False

    if l1 == 0:
        return equals_edit(s1,s2[1:],k-1)
    elif l1 == 0:
        return equals_edit(s1[1:],s2,k-1)

    if s1[0] == s2[0]:
        return equals_edit(s1[1:],s2[1:],k)
    else:
        return equals_edit(s1[1:],s2,k-1) or equals_edit(s1,s2[1:],k-1)



class EqualsTest(unittest.TestCase):
    def testEmpty(self):
        self.assertTrue(equals_edit("","",0))

    def testNotEmptyEqualsZeroTolerance(self):
        self.assertTrue(equals_edit("abc","abc",0))

    def testNotEmptyEqualsOneTolerance(self):
        self.assertTrue(equals_edit("abc","abc",1))

    def testDeleteOneTolerance(self):
        self.assertTrue(equals_edit("ab","abc",1))

    def testEditOneTolerance(self):
        self.assertTrue(equals_edit("ab","abc",1))

    def testDeleteZeroTolerance(self):
        self.assertFalse(equals_edit("ab","abc",0))

    def testEditZeroTolerance(self):
        self.assertFalse(equals_edit("ab","abc",0))


    def testEditLong(self):
        self.assertTrue(equals_edit("qwerqwerqwerqwerqwerqwerqwerqwerqw","qwerqwerqwerqwerqw1erqwerqwerqwerqw",1))

if __name__ == "__main__":
    unittest.main()